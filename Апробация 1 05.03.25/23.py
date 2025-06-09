c=0
def f(n,fl):
    if n==2 and fl:
        global c
        c+=1
    if n<2:
        return
    if n==16:
        fl=True
    f(n-2,fl)
    f(n//2,fl)

f(38,False)
print(c)