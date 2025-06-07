for n in range(1,1000):
    st=""
    n1=n
    c=0
    while n1!=0:
        c+=n1%10
        st=str(n1%2)+st
        n1//=2
    if c%2==0:
        st+="0"
    else:
        st+="1"
    n1 = r=int(st,2)
    c=0
    while n1!=0:
        c+=n1%10
        n1//=2
    if c%2==0:
        st+="0"
    else:
        st+="1"
    n1 = r = int(st, 2)
    c=0
    while n1!=0:
        c+=n1%10
        n1//=2
    if c%2==0:
        st+="0"
    else:
        st+="1"
    r=int(st,2)

    if r>2025:
        print(r,n,st)
