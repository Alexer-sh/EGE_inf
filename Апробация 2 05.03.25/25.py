import math

t=0
for n in range(700_001,1000000000):
    if t==5:
        break
    m=0
    for i in range(2,math.ceil(math.sqrt(n))):
        if n%i==0:
            m+=i
            m+=n//i
            break
    if m%10==4:
        print(n,m)
        t+=1