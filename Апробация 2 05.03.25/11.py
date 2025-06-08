import math

for n in range(1,1000):
    n1=math.ceil((n*11)/8)
    if n1*2000<=1024*693:
        print(n)