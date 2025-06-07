from itertools import product
s = product('012345678', repeat=5)
a = []
c = 0
for i in s:
    p=''.join(i)
    if p[0]!="0" and p.count("3")==1  and "35" not in p and "36" not in p and "37" not in p and "38" not in p and "53" not in p and "63" not in p and "73" not in p and "83" not in p:
        print(p)
        c+=1
print(c)