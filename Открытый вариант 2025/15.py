c=0
for A in range(1,11112):
    fl =True
    for x in range(0,1000):
        if not(((x&52!=0) and (x&48==0)) <= (not(x&A==0))):
            fl=False
            break
    if fl:
        c+=1
        print(A)
print(c)
