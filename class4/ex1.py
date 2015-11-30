#!/home/cdieken/applied_python/bin/python


import paramiko
import time
from getpass import getpass

def main():

    ip_addr = '50.76.53.27'
    username = 'pyclass'
    password = getpass()
    port = 8022

    remote_conn_pre = paramiko.SSHClient()

    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)

    remote_conn = remote_conn_pre.invoke_shell()

    remote_conn.send("term length 0\n")

    remote_conn.send("sh version\n")
    time.sleep(5)
    output = remote_conn.recv(5000)


    print output

if __name__ == "__main__":
    main()
