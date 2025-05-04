f=open("17_21712.txt").readlines()
a=[]
mn=111111111111
c=0
mx=0
for t in f:
    a.append(int(t))
    if 1000 <= int(t) < 10000 and int(t)%10==6 and int(t)<mn:
        mn=int(t)
print(mn)
for i in range(len(a)-2):
    b=[a[i],a[i+1],a[i+2]]
    c1=0
    for j in range(3):
        if abs(b[j])%10==6 and 1000<=abs(b[j])<10000:
            c1+=1
    if c1==1 and sum(b)<=mn:
        c+=1
        print(b)
        mx=max(mx,sum(b))
print(c,mx)