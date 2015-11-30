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

    pynet_rtr1 = ConnectHandler(**pynet1)
    pynet_rtr2 = ConnectHandler(**pynet2)
#    srx = ConnectHandler(**juniper_srx)


    for device in (pynet_rtr1, pynet_rtr2):

        output = device.send_command('sh run | inc logging buffered')
        print output

        output = device.send_config_from_file(config_file='file1.txt')

        time.sleep(2)

        output = device.send_command('sh run | inc logging buffered')
        print output

if __name__ == "__main__":
    main()
