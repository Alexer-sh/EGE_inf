f=open("9.6.txt").readlines()
d=0
for t in f:
    a=list(map(int,t.split(';')))
    b=[]
    c=[]
    fl1=False
    fl2=False
    if len(set(a))==5:
        for i in range(len(a)):
            if a.count(a[i])==3:
                break
            if a.count(a[i])!=1: #повторяющиеся
                fl1=True
                b.append(a[i])
            else:
                fl2=True
                c.append(a[i])
        if fl1 and fl2:
            if sum(a)/7>(sum(b)/len(b)):
                d+=1
                print(a)
print(d)