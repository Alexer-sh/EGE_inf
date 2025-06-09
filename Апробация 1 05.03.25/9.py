f=open("9 (2).txt").readlines()
c=0
a=[]
for t in f:
    c1=0
    c2=0
    s1=0
    s2=0
    b=list(map(int,t.split(';')))
    for i in range(6):
        if b.count(b[i])==3:
            c1+=1
            s1+=b[i]
        elif b.count(b[i])==1:
            c2+=1
            s2+=b[i]
    if c1==3 and c2==3 and s1**2 > s2**2:
        print(b)
        c+=1
print(c)