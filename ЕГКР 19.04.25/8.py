from itertools import product
s = product('АБДЕОП', repeat=6)
a = []
k = 1
for i in s:
    p=''.join(i)
    if p.count('О')==1 and p[0]=='О' and p.count('А')==1 and p.count('Б')==1 and p.count('Д')==1 and p.count('Е')==1 and p.count('П')==1 :
        a.append(k)
    k += 1
print(a)