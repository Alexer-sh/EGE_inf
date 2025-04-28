f=open("9.7.txt").readlines()
d=0
for t in f:
    a=list(map(int,t.split(';')))
    mx=max(a)
    b=[]
    c=[]
    if len(set(a))==5:
        for i in range(len(a)):
            if a[i]%2==0:
                b.append(a[i])#чётные
            else:
                c.append(a[i])
        if len(b)>len(c) and sum(b)<sum(c):
            d+=1
            print(a)
print(d)