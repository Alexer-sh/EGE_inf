from itertools import product
s = product('ДГИАШЭ', repeat=5)
a = []
k = 0
for i in s:
    p=''.join(i)
    if not(p[0]=='И' or p[0]=='А' or p[0]=='Э' or p[4]=='Д'or p[4]=='Г'or p[4]=='Ш'):
        a.append(p)
        k += 1
print(k)
print(a)