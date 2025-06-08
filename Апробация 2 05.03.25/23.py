c=0
def f(n,fl):
    if n==1 and fl:
        global c
        c+=1
    if n<=1:
        return
    if n==12:
        fl = True
    f(n-1,fl)
    f(n//2,fl)

f(30,False)
print(c)