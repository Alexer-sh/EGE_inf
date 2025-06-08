from ipaddress import *
c=0
net = ip_network("172.16.80.0/21", strict=False)
for ip in net:
    dv = bin(int(ip))[2:].zfill(32)
    if dv.count("1")%2!=0:
        c+=1


print(c)