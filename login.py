import ssh
import getpass
try:
    s = ssh.ssh()
    hostname = input('hostname: ')
    username = input('username: ')
    #password = getpass.getpass('password: ')
    s.login (hostname, username)
    s.sendline ('uptime')   # run a command
    s.prompt()             # match the prompt
    print(s.before)          # print everything before the prompt.
    s.sendline ('ls -l')
    s.prompt()
    print(s.before)
    s.sendline ('df')
    s.prompt()
    print(s.before)
    s.logout()
except (ssh.Exceptionssh, 'e'):
    print ("pxssh failed on login.")
    print(str('e'))
