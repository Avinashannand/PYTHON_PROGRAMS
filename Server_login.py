import spur
import os

shell = spur.SshShell(hostname="x.x.x.x", username="user", password="pass")

#temp=os.popen(cmd).read()
#list=temp.rstrip()

result = shell.run(["ps", "-ef", "|", "grep paytm", "|", "awk", "'{print $2}'"])
print(result)  #print the result

'''
try:
    shell = spur.SshShell("x.x.x.x",
                      "user",
                      "pass",
                       missing_host_key=spur.ssh.MissingHostKey.accept)

    with shell:
        result = shell.run(["ls"])
        print(result)
except os.error:
    print(error)
    raise'''




