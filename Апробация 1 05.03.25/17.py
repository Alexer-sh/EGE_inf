f=open("17_17558.txt").readlines()
c=0
mx=0
k=0
a=[]
for t in f:
    n=int(t)
    if n%32==0:
        k+=1
    a.append(n)
for i in range(len(a)-1):
    if (a[i]<0 or a[i+1]<0) and a[i+1]+a[i]<k:
        c+=1
        mx=max(mx,a[i]+a[i+1])
        print(a[i],a[i+1])
print(c,mx)