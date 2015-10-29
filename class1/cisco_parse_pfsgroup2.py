#!/home/cdieken/applied_python/bin/python

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco.txt")

pfs_group = cisco_cfg.find_objects(r"set pfs group2")

for c_map in pfs_group:
    print
    parent = c_map.parent
    print parent.text
print

