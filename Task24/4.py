st=input()
mx=0
c=1
b=[]
st=st.replace("KL"," ")
st = st.replace("LK"," ")
for i in range(1,len(st)):
    if st[i]!=" ":
        c+=1
    else:
        if c>mx:
            mx=c
        c=1
if c>mx:
    mx=c
print(mx+1,sep='')