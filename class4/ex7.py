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
#    srx = ConnectHandler(**juniper_srx)


    output = pynet_rtr2.send_command('sh run | inc logging buffered')
    print output

    config_commands = ['logging buffered 234123']

    output = pynet_rtr2.send_config_set(config_commands)

    time.sleep(2)

    output = pynet_rtr2.send_command('sh run | inc logging buffered')
    print output

if __name__ == "__main__":
    main()
