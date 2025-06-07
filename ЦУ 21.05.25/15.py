c=0
for A in range(1,11112):
    fl =True
    for x in range(1,1000):
        if not(((x%2==0) <= (not (x%5==0))) or (x+A >=90)):
            fl=False
            break
    if fl:
        print(A)
        break

