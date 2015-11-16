#!/home/cdieken/applied_python/bin/python

from snmp_helper import snmp_get_oid, snmp_extract
import getpass

sysDescr = '1.3.6.1.2.1.1.1.0'
sysName = '1.3.6.1.2.1.1.5.0'


def main():

#    ip_addr = raw_input("IP address: ")
#    ip_addr = ip_addr.strip()
#    community_string = getpass.getpass(prompt="Community String: ")

    ip_addr = '50.76.53.27'
    community_string = "galileo"
    
    pynet_rtr1 = (ip_addr, community_string, 7961)
    pynet_rtr2 = (ip_addr, community_string, 8061)

    for a_device in (pynet_rtr1, pynet_rtr2):

        print "\n***********************"
        for the_oid in (sysName, sysDescr):
            snmp_data = snmp_get_oid(a_device, oid=the_oid)
            output = snmp_extract(snmp_data)
            
            print output
        print "***********************"

    print


if __name__ == "__main__":
    main()

