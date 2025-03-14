st = open("24_demo.txt").readline()
c=0
mx=1
print(st)
for i in range(len(st)):
    if st[i]=='Y':
        c+=1
    else:
        if c>mx:
            mx=c
        c=0
if c>mx:
    mx=c
print(mx)
