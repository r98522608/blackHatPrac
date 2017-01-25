"""
Working in both python3.5 & python2.7
Before using, need pip install ipy
"""
import shlex
import subprocess
import sys
try:
    from IPy import IP
except ImportError:
    print("No IPy package!")
    sys.exit(1)
# else:
#     sys.exit(0)


mypath = '/etc/hosts'
fp = open(mypath)
for line in fp.readlines():
    ip = line.rstrip()
    ips = ip.split()
    if ips:
        try:
            IP(ips[0])
        except:
            print("The ip \"{}\"is not valid!".format(ips[0]))
        else:
            tmp_cmd = "ping -c1 {0}".format(ips[0])
            cmd = shlex.split(tmp_cmd)
            try:
                output = subprocess.check_output(cmd)
            except subprocess.CalledProcessError as e:
                print ("The IP {0} is NotReacahble".format(cmd[2]))
            else:
                print ("The IP {0} is Reachable".format(cmd[2]))

