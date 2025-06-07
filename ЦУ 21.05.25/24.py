f=open("zadacha-24-6ba07684-4454-436e-8147-5ba42fb16ef4.txt").readline()
c=1
c_s=f[0]
a=1
for i in range(1,len(f)):
    if f[i]==f[i-1]:
        a+=1
    else:
        if a>=c:
            c=a
            c_s=f[i-1]
            print(c,f[i-1])
        a=1
print(c)