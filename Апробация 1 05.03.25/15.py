mx=0
for A in range(1,10000):
    fl=True
    for x in range(1,1000):
        B = 60<=x<=80
        if not(x%A==0 or (B <=(not (x%22==0)))):
            fl=False
    if fl:
        mx=A
print(mx)