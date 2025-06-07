f = open("9.txt").readlines()
c=0
for t in f:
    a=list(map(int,t.split(';')))
    c1=0
    c2=0
    s=0
    for i in range(7):
        if a.count(a[i])==2:
            c2+=1
        if a.count(a[i])==1:
            c1+=1
            s+=a[i]
    if c2==4 and c1==3 and s/3 <= sum(a)/7:
        c+=1
        print(a)
print(c)