"""
Обозначим через
ДЕЛ(n,m) утверждение «натуральное число
n делится без остатка на натуральное число
m». Сколько существует натуральных значений
A на отрезке
[1;11111], для которых выражение
(ДЕЛ(A,x)→(x≡A)∨(x≡1))∀x∈N
тождественно истинне (т. е. принимает значение 1)?
"""
c=0
for A in range(1,11112):
    fl =True
    for x in range(1,10000):
        if not( (A%x==0) <= (x==A or (x==1))):
            fl=False
            break
    if fl:
        c+=1
        print(A)
print(c)
