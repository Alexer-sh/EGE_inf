c=0
def f(n,fl):
    if n ==24 and fl:
        global c
        c+=1
        return
    if n>24:
        return
    if n==11:
        fl=True
    if n==12 and fl:
        return
    if n==12:
        fl=True
    f(n+1,fl)
    f(n*2,fl)
f(2,False)
print(c)
