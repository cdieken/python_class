#!/home/cdieken/applied_python/bin/python

# create a list with a dictionary with at least two keys.  Write list
# out to a file using both YAML and JSON.  YAML should be expanded.


import yaml
import json

my_list = range(8)
my_list.append('cisco')
my_list.append('juniper')
my_list.append('brocade')
my_list.append({})
my_list[-1]['ip_cisco'] = '10.1.1.1'
my_list[-1]['ip_juniper'] = '10.2.1.1'
my_list[-1]['ip_brocade'] = '10.3.1.1'
my_list.append({})
my_list[-1]['iterate'] = range(5)

with open("class1.yml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))


