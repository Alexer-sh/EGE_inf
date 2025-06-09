import math

for n in range(1,100):
    n1=n*248
    n2=math.ceil(n1/8)
    if n2*75600>16*1024*1024:
        print(n)