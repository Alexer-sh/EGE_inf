f = open("9 (5).txt")
r =f.readlines()
c=0
for t in r:
    a=list(map(int,t.split(';')))
    b=0
    for i in range(6):
        if a[i]%2==1:
            b+=1
    if (len(set(a))<6) != (b==3):
        c+=1
print(c)
