st = open("24 (2).txt").readline()
mx=0
c=1
b=[0]*27
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(0,len(st)-2):
    if st[i]==st[i+2]:
        b[int(st[i+1],36)-10]+=1
t=max(b)
for i in range(len(b)):
    if b[i]==t:
        print(letters[i])
        break
#Искуство говнокода