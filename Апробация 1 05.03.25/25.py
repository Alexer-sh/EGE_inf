t=0
for n in range(500_000,1_000_000):
    if t==5:
        break
    r=0
    for i in range(2,n):
        if n%i==0:
            r+=i
    if r%10==9:
        t+=1
        print(n,r)
