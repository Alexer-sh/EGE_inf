for n in range(4,10000):
    s="4"+n*"2"
    while "42" in s or "8222" in s or "2222" in s:
        if "42" in s :
            s=s.replace("42","2",1)
        if "8222" in s :
            s=s.replace("8222","24",1)
        if "2222" in s:
            s = s.replace("2222", "8", 1)
    st1=int(s)
    c=0
    while st1>0:
        c+=st1%10
        st1=st1//10
    print(c)
    if c==110:
        print(n)
        break