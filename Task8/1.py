from itertools import product
s = product('АБРТЫ', repeat=5)
a = []
k = 1
for i in s:
    p=''.join(i)
    if p.count('Ы')==0 and p.count('АА')==0:
        a.append(k)
    k += 1
print(k)