c=0
def f(n):
    if n ==14:
        global c
        c+=1
        return
    if n>14 or n==5 or n ==10:
        return
    f(n+1)
    f(n+3)
    f(n*2)
f(2)
print(c)