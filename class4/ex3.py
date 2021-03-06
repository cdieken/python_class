#!/home/cdieken/applied_python/bin/python

import pexpect
from getpass import getpass


def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    port = 8022
    password = getpass()


    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    ssh_conn.expect('pynet-rtr2#')

    ssh_conn.sendline('sh ip int brief')
    ssh_conn.expect('pynet-rtr2#')
    print ssh_conn.before

if __name__ == "__main__":
    main()
