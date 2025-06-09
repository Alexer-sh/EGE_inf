def f(n,h):
    if n>=51 and h==3:
        return 1
    if n>51:
        return 0
    if h>3:
        return 0
    if h%2==0:  #Ход Вани
        return f(n+1,h+1) + f(n+4,h+1) + f(n*2,h+1)
    else:
        return f(n + 1, h + 1) * f(n + 4, h + 1) * f(n * 2, h + 1)


for s in range(1,50):
    if f(s,1):
        print(s)
