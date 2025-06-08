n=3**100
for x in range(2030,1,-1):
    st=""
    n1=n-x
    while n1>0:
        st=str(n1%3)+st
        n1//=3
    if st.count("0")==1:
        print(x,st)
        break