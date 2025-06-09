for n in range(1,2000):
    st=''
    n1=n
    while n1>0:
        st=str(n1%2)+st
        n1//=2
    if n%2==0:
        st="10"+st
    else:
        st="1"+st
        st+="01"
    r=int(st,2)
    if n<=12:
        print(r)