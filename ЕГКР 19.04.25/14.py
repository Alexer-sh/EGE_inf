n = 4**210+4**110
c=0
for x in range(1,3000):
    n1=n-x
    st = ""
    while n1 > 0:
        st = str(n1 % 4) + st
        n1 = n1 // 4
    #print(st)
    if st.count('0')>c:
        c=st.count('0')
        print(x,c)
