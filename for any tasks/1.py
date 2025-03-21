from itertools import product
s='AДМТ'
a=product(s,repeat=5)
b=list(a)
for i in range(len(b)):
    if i==331:
        print(b[i])
