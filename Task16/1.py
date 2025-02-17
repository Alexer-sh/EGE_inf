from sys import *
setrecursionlimit(100000)
def f(n):
    if n ==1:
        return 2
    else:
        return f(n-1)+5*n**2
print(f(39))