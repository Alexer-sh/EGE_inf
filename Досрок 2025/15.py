for A in range(0,10000):
    fl=True
    for x in range(0,100):
        for y in range(0,100):
            if not((5<y) or (x>32) or (x+2*y <A)):
                fl=False
    if fl:
        print(A)
        break