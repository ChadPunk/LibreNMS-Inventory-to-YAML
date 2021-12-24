import requests
import json 


# Set LibreNMS API key, URL, and inventory file
device = ''
url_devices = 'http://10.77.8.3:8000/api/v0/devices/'
groupsurl = 'http://10.77.8.3:8000/api/v0/devicegroups/'

# Change Me!!!
api_key = '123456'
hosts_file = 'hosts'

# Pass authentication token
headers={
    'X-Auth-Token': api_key
}

# Initial API call to get devices
librenms = requests.get(url_devices, headers=headers)

# Open hosts file
ansible_inventory_file = open(hosts_file, "w")

# Write initial information
ansible_inventory_file.write("#Ansible dynamic inventory file generated from Netbox API\n")
ansible_inventory_file.write("\n")
ansible_inventory_file.write("all:\n")
ansible_inventory_file.write("  hosts:\n")


for item in librenms.json()['devices']:
    deviceName = item['hostname']
    ip = item['hostname']
    name = item['sysName']
    ansible_inventory_file.write('    ' + name + ':\n')
    ansible_inventory_file.write('      ' + 'ansible_host' + ': ' + ip + '\n')


# Create device groups from LibreNMS
ansible_inventory_file.write("  children:\n")

groups = requests.get(groupsurl, headers=headers)
for groups in groups.json()['groups']:
    group = groups['name']
    ansible_inventory_file.write('    ' + group + ':' + '\n')
    ansible_inventory_file.write("       hosts:\n")
    librenmsgroup = requests.get(groupsurl + group, headers=headers)
    resp = librenmsgroup.json()
    print(group)
    try:
        for device in librenmsgroup.json()['devices']:
            deviceid = str(device['device_id'])
            librenmsgroup = requests.get(url_devices + deviceid, headers=headers)
            for item in librenmsgroup.json()['devices']:
                name = item['sysName']
                ansible_inventory_file.write('      ' + name + ':\n')
                print(item['sysName'])
    except KeyError:
        print("No group detected")


