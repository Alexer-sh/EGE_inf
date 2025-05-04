for n in range(3,1000):
    st=""
    n1=n
    while n1>0:
        st=str(n1%3)+st
        n1=n1//3
    if n%3==0:
        st+=st[:2]
    else:
        if n%3==1:
            st+="10"
        elif n%3==2:
            st+="20"
    if int(st,3)<150:
        print(st,n,int(st,3))
    else:
        break