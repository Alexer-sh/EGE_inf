f = open("17_1.txt", encoding="utf-8-sig")
a = [int(i.strip()) for i in f]
f.close()
c=0
mx=0
for i in range(len(a)-1):
    if (abs(a[i])%4==0 or abs(a[i+1])%4==0) and (abs(a[i]+a[i+1])%7==0):
        c+=1
        print(a[i],a[i+1])
        if a[i]+a[i+1]>mx:
            mx=a[i]+a[i+1]
print(c,mx)