import math

t=0
for n in range(1000_000_001,2000_000_001):
    if t==5:
        break
    c=0
    s=0

    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            s+=n//i
            if c==0:
                s+=i
                c+=1
            else:
                break
    fl=True
    if s!=0:
        for m in range(2,int(math.sqrt(s))+1):
            if s%m==0:
                fl=False
                break
        if fl:
            t+=1
            print(n,s)