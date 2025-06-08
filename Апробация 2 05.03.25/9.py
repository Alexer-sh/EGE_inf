f=open("9.txt").readlines()
c=0
for t in f:
    a=list(map(int,t.split(";")))
    c1=0
    for i in range(4):
        if a.count(a[i])==2:
            c1+=1
    if max(a)<sum(a)-max(a) and c1==2:
        print(a)
        c+=1
print(c)