f=open("9.txt")
r=f.readlines()
c=0
for t in r:
    a= list(map(int,t.split(';')))
    fl1=0
    b=0 #Неповтор
    d=[]
    for i in range(7):
        if a.count(a[i])==3:
            fl1+=1
        if a.count(a[i])==1:
            b=a[i]
        else:
            d.append(a[i])
    if fl1==6 and max(d)>b:
        print(a)
        c+=1

print(c)