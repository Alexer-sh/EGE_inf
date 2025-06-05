
for n in range(1,1000):
    st=""
    n1=n
    c=0
    while n1!=0:
        c+=n1%2
        st=str(n1%2)+st
        n1//=2
    if c%2==0:
        st+="00"
    else:
        st+="10"
    r=int(st,2)
    print(r, n, st)
    if r>253:
        print(r,n,st)
        break