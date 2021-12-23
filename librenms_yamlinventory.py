import requests
import json 
import sys
import ruamel.yaml

# Set LibreNMS API key, URL, and inventory file
# Change Me!!!
url_devices = 'http://10.77.8.3:8000/api/v0/devices/'
groupsurl = 'http://10.77.8.3:8000/api/v0/devicegroups/'

# Change Me!!!
api_key = '12345'
hosts_file = 'hosts'

# Pass authentication token
headers={
    'X-Auth-Token': api_key
}

# Initial API call to get devices
librenms = requests.get(url_devices, headers=headers)


# Init Dictionary
librenmsDict = {}
librenmsDict['all'] = {}
librenmsDict['all']['hosts'] = {}
librenmsDict['all']['children'] = {}

# Set Dictionary
for item in librenms.json()['devices']:
    deviceName = item['hostname']
    ip = item['hostname']
    name = item['sysName']
    librenmsDict['all']['hosts'][name] = {}
    librenmsDict['all']['hosts'][name]['ansible_host'] = ip


# # Create device groups from LibreNMS
groups = requests.get(groupsurl, headers=headers)
for groups in groups.json()['groups']:
    group = groups['name']
    librenmsDict['all']['children'][group] = {}
    librenmsDict['all']['children'][group]['hosts'] = []
    librenmsgroup = requests.get(groupsurl + group, headers=headers)
    resp = librenmsgroup.json()
    try:
        for device in librenmsgroup.json()['devices']:
            deviceid = str(device['device_id'])
            librenmsgroup = requests.get(url_devices + deviceid, headers=headers)
            for item in librenmsgroup.json()['devices']:
                name = item['sysName']
                librenmsDict['all']['children'][group]['hosts'].append(name)
    except KeyError:
        print("No group detected for " + item['sysName'])

# Open hosts file
ansible_inventory_file = open(hosts_file, "w")

# Write YAML
ansible_inventory_file.write("#Ansible dynamic inventory file generated from Netbox API\n")
ansible_inventory_file.write("\n")
ansible_inventory_file.write((ruamel.yaml.dump(librenmsDict, Dumper=ruamel.yaml.RoundTripDumper).replace('{}', '',)))




