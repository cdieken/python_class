#!/home/cdieken/applied_python/bin/python

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco.txt")

crypto_lines = cisco_cfg.find_objects(r"^crypto map CRYPTO")

print "crypto map groups:\n"

for i in crypto_lines:
    print i.text

print "\nDetail:\n"

for c_map in crypto_lines:
    print
    print c_map.text
    for child in c_map.children:
        print child.text
print
