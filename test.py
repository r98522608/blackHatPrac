#with open("ip.txt") as f:
#    content = f.readlines()
#    print "the ip is %s" % content


ips = [ip.rstrip('\n') for ip in open('ip.txt')]

#for i in ips:
#    print "the ip is %s" % i
