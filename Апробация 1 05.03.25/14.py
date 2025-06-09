n=7**170+7**100
mx=0
for x in range(2030,0,-1):
    n1=n-x
    st=""
    while n1>0:
        st=str(n1%7)+st
        n1//=7

    if st.count('0')>mx:
        mx=st.count('0')
        print(x,mx,st)