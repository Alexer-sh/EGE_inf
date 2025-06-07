f=open("zadacha-17-709d9a65-34a4-4b94-a36e-f1071d5f6c5f.txt").readlines()
a=[]
b1=[]
mn110=1000000000000
for t in f:
    t1=int(t)
    a.append(int(t))
    if int(t)%110==0 and int(t)>0 :
        mn110=min(mn110,int(t))
c=0
mn=-10000000000000
print(mn110)
for i in range(len(a)-1):
    if a[i]+a[i+1]<mn110:
        c+=1
        mn=max(mn,a[i]+a[i+1])
        print(a[i],a[i+1])
print(c,abs(mn))
