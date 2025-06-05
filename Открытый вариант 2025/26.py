f = open("26_21910.txt").readlines()
a=[]
for t in f:
    a.append(int(t))
a.sort(reverse=True)
c=0
b=a[0]
for i in range(1,len(a)):
    if abs(a[i]-b)>=9:
        c+=1
        b=a[i]
print(c,b,a)