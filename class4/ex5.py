#!/home/cdieken/applied_python/bin/python

import time
from netmiko import ConnectHandler
from getpass import getpass


def main():

    password = getpass()

    pynet1 = {
        'device_type': 'cisco_ios',
        'ip': '50.76.53.27',
        'username': 'pyclass',
        'password': password,
    }

    pynet2 = {
        'device_type': 'cisco_ios',
        'ip': '50.76.53.27',
        'username': 'pyclass',
        'password': password,
        'port': 8022,
    }

    juniper_srx = {
        'device_type': 'juniper',
        'ip': '50.76.53.27',
        'username': 'pyclass',
        'password': password,
        'secret': '',
        'port': 9822,
    }

#    pynet_rtr1 = ConnectHandler(**pynet1)
    pynet_rtr2 = ConnectHandler(**pynet2)
    time.sleep(5)
#    srx = ConnectHandler(**juniper_srx)

    pynet_rtr2.config_mode()
    time.sleep(5)
    output = pynet_rtr2.check_config_mode()
    print "\nConfig mode? (true/false):"
    print output

if __name__ == "__main__":
    main()
