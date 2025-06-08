f=open("17_17873.txt").readlines()
c=0
a=[]
for t in f:
    a.append(int(t))
mn=min(a)%16
mx_s=-1
for i in range(len(a)-1):
    if a[i]%16==mn or a[i+1]%16==mn:
        c+=1
        mx_s=max(mx_s,a[i]+a[i+1])
print(c,mx_s)