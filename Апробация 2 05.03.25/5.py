for n in range(1, 1000):
    n1 = n
    st = ""
    while n1 > 0:
        st = str(n1 % 2) + st
        n1 //= 2

    if st.count("1") % 2 == 0:
        st += "0"
        st = '10' + st[2:]
    else:
        st += "1"
        st = '11' + st[2:]

    r = int(st, 2)
    print(r, n, st)