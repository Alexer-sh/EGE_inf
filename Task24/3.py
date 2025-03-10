st = open('24 (1).txt').readline()
c=1
mx=0
st=st.replace("PP"," ")
for i in range(1,len(st)):
    if st[i]!=" ":
        c+=1
    else:
        if c>mx:
            mx=c+1
        c=1
if c>mx:
    mx=c+1
print(mx,sep='')