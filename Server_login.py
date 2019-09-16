#import socket
#import libssh2
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect(('exmaple.com', 22))
#session = libssh2.Session()
#session.startup(sock)
#session.userauth_password('john', '******')
#channel = session.channel()
#channel.execute('ls -l')
#print(channel.read(1024))
#shell = spur.SshShell(hostname="10.140.32.144", username="dev", password="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDahpVVNCBIeWfFi2smtMVxvNk3X20DIR/463IZ3edjIGY1y5rfiooSjD5ipc0H6hlQFrA02JLldrIIcRlGKsJ5Mq/JrFD7zSh+PBr9J1zPa3SWIjPnf+i7SH/+vw17xlMnGGJwGqcj+HkNrmpFJ9KrPEMgkdEswF+0RMPJFOxC91Oo6NWSGS0Qrk1EMZWSEb6+HcLvl/BY6xca1HqZffoidyRMJOzgSr8quB93O+y/EDxaVQGgGiIVkNkbpq5XAOI1+DUwPIegPim8j45ziT7z3LWB6X4dTG50SCQoOZ7JYQZxrvRC5VM2CIiDaB0HbTw7cDjPgF/XRLCGqC2GCn8N avinash@197NODNB")

import spur
import os

shell = spur.SshShell(hostname="10.142.52.100", username="root", password="walletpaytm@123")

#temp=os.popen(cmd).read()
#list=temp.rstrip()

result = shell.run(["ps", "-ef", "|", "grep paytm", "|", "awk", "'{print $2}'"])
print(result.output)  #print the result




