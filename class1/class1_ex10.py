#!/home/cdieken/applied_python/bin/python

import re
from ciscoconfparse import CiscoConfParse


cisco_cfg = CiscoConfParse("cisco.txt")

crypto_line = cisco_cfg.find_objects_wo_child(r"^crypto map CRYPTO", r"AES")

'''
for line in crypto_line:
    print 
    print line.text
    for child in line.children:
        print child.text
print
'''

print "\nCrypto maps not using AES:"
for line in crypto_line:
    for child in line.children:
        if 'transform' in child.text:
            match = re.search(r"set transform-set (.*)$", child.text)
            encryption = match.group(1)
    print "  {0} >>> {1}".format(line.text.strip(), encryption)
print

