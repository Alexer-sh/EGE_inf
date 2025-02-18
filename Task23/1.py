c=0
def f(n):
    if n ==15:
        global c
        c+=1
        return
    if n>15:
        return
    f(n+1)
    f(n+3)
f(2)
print(c)