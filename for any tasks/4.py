f = open("26.txt")
a = f.readline()
n,m =a.split()
m=int(m)
b = [int(i.strip()) for i in f]
b.sort()
t=0
for i in range(len(b)):
    if b[i]>=210 and b[i]<=220:
        m-=b[i]
        t+=1
print(m,t)
for i in range(len(b)):
    if m>0:
        m-=b[i]
        t+=1
print(m,t)