f=open("26_21424.txt").readlines()
n=int(f[0])
a=[]
for i in range(1,len(f)):
    a.append(int(f[i]))
a.sort(reverse=True)
c=0
b=[]
i=0
b.append(a[0])
while i<10000:
    if b[len(b)-1]-a[i]>=9:
       b.append(a[i])
    i+=1
print(b)
print(len(b))
#примитивнейшая задача