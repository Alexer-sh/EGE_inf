st=input()
mx=0
c=1
mx_a=''
b=[]
for i in range(1,len(st)):
    if st[i]==st[i-1]:
        c+=1
    else:
        if c>mx:
            mx=c
            mx_a=st[i-1]
        c=1
if c>mx:
    mx=c
    mx_a=st[len(st)-1]
print(mx_a,mx,sep='')