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
    srx = ConnectHandler(**juniper_srx)

    time.sleep(5)

    for device in (pynet_rtr1, pynet_rtr2, srx):

        print device
        output = device.send_command("sh arp")
        time.sleep(5)
        print output


if __name__ == "__main__":
    main()
