num=7**350 + 7**150
for x in range(2300,1,-1):
    n=num-x
    n1=n
    st=''
    while n1>0:
        st=str(n1%7)+st
        n1//=7

    if st.count('0')==200:
        print(x)
        print(st)
        break

