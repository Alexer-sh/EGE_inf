from ipaddress import *
c=0
net = ip_network("105.224.200.224/27", strict=False)
for ip in net:
    dv = bin(int(ip))[2:].zfill(32)
    if dv.count("1")%4==0:
        c+=1


print(c)
