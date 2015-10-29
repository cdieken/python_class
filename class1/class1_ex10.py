#!/home/cdieken/applied_python/bin/python

from ciscoconfparse import CiscoConfParse


cisco_cfg = CiscoConfParse("cisco.txt")

crypto_line = cisco_cfg.find_objects_wo_child(r"^crypto map CRYPTO", r"AES")

for line in crypto_line:
    print 
    print line.text
    for child in line.children:
        print child.text
print

