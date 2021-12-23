# LibreNMS-Inventory-to-YAML
This script will let you make an API call to LibreNMS to pull device groups and devices within those groups. This file can then be used in an Ansible inventory. These scripts could use some cleaning up so feel free to tweak them to achieve your desired goal.

There are two scripts. They both function a little differently but achieve the same goal. 
<b>librenms_yamlinventory.py</b> uses the <b>ruamel.yaml</b> package and will be required to run the script. This package handles all of the format that is required for YAML.
<b>librenms_getinventory.py</b> is spaced manually and shouldn't require any additional item to be ran, use this for testing if the other fails for you.


<li>
To install ruamel.yaml, Run: 
<b>pip install ruamel.yaml</b>
  *only if you plan on using <i>librenms_yamlinventory.py</i>
</li>

<li>
Then clone or copy the desired script to your folder:
<b>git clone (url goes here)</b>
</li>

<li>
Replace the URLs, API Key, and hosts files varibale with your infromation.
</li>
