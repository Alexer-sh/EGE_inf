from itertools import product
alf="КОСУФ"
a=product(alf,repeat=5)
k=0
for t in a:
    k+=1
    s=''.join(t)
    if s.count("У")==2 and s.count("Ф")==0:
        print(s,k)