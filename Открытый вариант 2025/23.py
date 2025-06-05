c=0
def f(n,fl):
    if n==18 and fl == True:
        global c
        c+=1
        return
    if n>18:
        return
    if n==14:
        fl=True
    if n==8:
        return
    f(n+1,fl)
    f(n+2,fl)
    f(n*2,fl)

f(3,False)
print(c)