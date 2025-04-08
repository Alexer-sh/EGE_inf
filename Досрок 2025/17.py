f=open("17_21416.txt")
r=f.readlines()
a=[]
sm=0
c=0
mx=0
for t in r:
    a.append(int(t))
    if int(t)<0:
        sm+=int(t)
for i in range(len(a)-2):
    b=[a[i],a[i+1],a[i+2]]
    if max(b)*min(b) >sm:
        c+=1
        mx=max(mx,sum(b))
print(c,mx,len(r))
