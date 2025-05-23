"""
На числовой прямой даны три отрезка: D = [15; 40], C = [21; 63] и А = [7; E].
Укажите наименьшее возможное целое значение E такое, что формула
(x∈D)→((¬(x∈C)∧¬(x∈A))→¬(x∈D))
истинна (то есть принимает значение 1 при любом значении переменной х).
"""

def f(x,a1,a2):
    A = a1<=x<=a2
    D = 15<= x <=40
    C = 21<=x<=63
    return (D)<=((not(C) and (not (A))) <=(not(D)))

ox = [y for x in (14,40,21,63) for y in (x,x+0.01,x-0.01)]

m=[]
for a2 in ox:
    if a2>7 and all(f(x,7,a2) ==1 for x in ox):
        m.append(a2)
print(min(m))
#Тут 21