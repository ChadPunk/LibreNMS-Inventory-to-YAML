# LibreNMS-Inventory-to-YAML
This script will let you make an API call to LibreNMS to pull device groups and devices within those groups. This file can then be used in an Ansible inventory. This scripts could use some work so feel free to clean it up.

There are two scripts. They both function a little differently but achieve the same goal. 
<b>librenms_yamlinventory.py</b> uses the <b>ruamel.yaml</b> package and will be required to run the script.
<b>librenms_getinventory.py</b> is spaced manually and shouldn't require any additional item to be ran.


<li>
To install ruamel.yaml, Run: 
<b>pip install ruamel.yaml</b>
</li>

<li>
Then clone or copy the desired script to your folder:
<b>git clone (url goes here)</b>
</li>

<li>
Replace the URLs, API Key, and hosts files varibale with your infromation.
</li>
