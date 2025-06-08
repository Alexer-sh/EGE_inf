def f(x,a1,a2):
    A = a1<=x<=a2
    D = 17<= x <=58
    C = 29<=x<=80
    return D <=((C and (not A)) <= (not D))

ox = [y for x in (17,58,29,80) for y in (x,x+0.01,x-0.01)]

m=[]
for a1 in ox:
    for a2 in ox:
        if a2>a1 and all(f(x,a1,a2) ==1 for x in ox):
            m.append(a2-a1)
print(min(m))
#Я хз по какому принципу это работает, но работает же
