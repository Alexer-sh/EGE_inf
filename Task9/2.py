f = open("9 (3).txt")
r=f.readlines()
c=0
for t in r:
    a=list(map(int,t.split(';')))
    if a[1]**2-4*a[0]*a[2]>0:
        c+=1
print(c)