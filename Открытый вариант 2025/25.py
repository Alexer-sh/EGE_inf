t=0
for n in range(500_001,1000_000):
    if t>5:
        break
    m=0
    for i in range(1,n+1):
        if n%i==0:
            m+=i
    if m%10==6:
        print(m,n)
        t+=1