from ipaddress import *
ad = ip_address("124.68.23.175")
net2 = ip_network("234.68.125.0/28")  # сеть №2, маска задана количеством 1
net3 = ip_network("234.68.125.125/28", False)  # сеть №3, адрес сети будет вычислен (ip узла & маску)
net = ip_network("234.68.125.0/29")
for ad in net:
    print(ad)