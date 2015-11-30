#!/home/cdieken/applied_python/bin/python

import pexpect
import sys
import re
from getpass import getpass

def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    port = 8022
    password = getpass()

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    #ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    ssh_conn.expect('#')

    ssh_conn.sendline('sh ip int brief')
    ssh_conn.expect('#')
    print ssh_conn.before

    ssh_conn.sendline('terminal length 0')
    ssh_conn.expect('#')
    print ssh_conn.before
    
    ssh_conn.sendline('sh version')
    ssh_conn.expect('pynet-rtr2#')
    print ssh_conn.before
    print ssh_conn.after

    try:
        ssh_conn.sendline('show run')
        ssh_conn.expect('pynet-rtr2#')
        print ssh_conn.before
    except pexpect.TIMEOUT:
        print "Found timeout"

    pattern = re.compile(r'^Lic.*DI:.*$', re.MULTILINE)
    ssh_conn.sendline('show version')
    ssh_conn.expect(pattern)
    print ssh_conn.after

if __name__ == "__main__":
    main()
