from ipaddress import *
net = ip_network("123.45.34.28/28",0)
print(net.network_address)
net = ip_network("123.45.34.28/28",0)
print(net.num_addresses)
net = ip_network("123.45.34.28/28",0)
print(net.netmask)
ad = ip_address("124.68.23.175")
print(bin(int(ad))[2:].zfill(32))
for mask in range(33):
    net = ip_network("23.124.57.19/"+str(mask), 0)
    print(net)