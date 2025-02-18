f=open("9 (2).txt")
r=f.readlines()
c=0
for t in r:
    a= list(map(int,t.split(';')))
    if max(a) == a[0]:
        if a[0]**2 == a[1]**2+a[2]**2:
            c+=1
    elif max(a)==a[1]:
        if a[1]**2 == a[0]**2+a[2]**2:
            c+=1
    else:
        if a[2]**2 == a[1]**2+a[0]**2:
            c+=1

print(c)