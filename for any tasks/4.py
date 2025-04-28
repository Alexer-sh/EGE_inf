f=open("9.4.txt").readlines()
d=0
for t in f:
    a=list(map(int,t.split(';')))
    mx=max(a)
    b=[]
    c=0
    fl1=False
    fl2=False
    if a.count(mx)==1 and len(set(a))!=len(a):
        if ((sum(a)-mx)/5)*3 < mx:
            d+=1
            print(a)
print(d)