#!/home/cdieken/applied_python/bin/python

import yaml
import json

print "\n\nworking on YAML print:\n\n"

with open("class1.yml") as f:
    new_list = yaml.load(f)

print yaml.dump(new_list, default_flow_style=False)

print "\n\nworking on JSON print:\n\n"

with open("class1.json") as f:
    new_list = json.load(f)

from pprint import pprint as pp

pp(new_list)

print "\n\nend of program\n\n"
