for n in range(3,10000):
    s="1"+n*"9"
    while "19" in s or "399" in s or "999" in s:
        if "19" in s :
            s=s.replace("19","9",1)
        if "399" in s :
            s=s.replace("399","91",1)
        if "999" in s:
            s = s.replace("999", "3", 1)
    st1=int(s)
    c=0
    while st1>0:
        c+=st1%10
        st1=st1//10
    #print(c)
    if c==33:
        print(n)
        print(s)