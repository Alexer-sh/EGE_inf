t = open('demo_2025_24.txt').read()
t = t.replace('-', '*')
t = t.replace('*0*', '*5*')
t = t.replace('**', 'x')
t = t.replace('*0', 'x')
t = t.replace('x0', 'x')
t = t.replace('x*', 'x')
t = t.replace('*x', 'x')
a = t.split('x')
k=0
for i in a:
    if len(i)>3:
        k = max(k,len(i))
print(k)
#Это писал не я, но я бы написал схожим образом (наверное)