for n in range(1,1000):
    st=bin(n)[2:]
    if st.count('1')%2==0:
        st+='0'
        st="10"+st[2:]
    else:
        st += '1'
        st = "11" + st[2:]
    r=int(st,2)
    print(n,st,r)
    if r>480:
        print(n)
        break

