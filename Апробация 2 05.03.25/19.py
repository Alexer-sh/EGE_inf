def f(n1,n2,h):
    if n1+n2>=81 and h==3:
        return 1
    if n1+n2>81:
        return 0
    if h>3:
        return 0
    if h%2==1:  #ход Пети
        return f(n1+1,n2,h+1) + f(n1*2,n2,h+1) + f(n1,n2+1,h+1) + f(n1,n2*2,h+1)
    else:
        return f(n1 + 1, n2, h + 1) + f(n1 * 2, n2, h + 1) + f(n1, n2 + 1, h + 1) + f(n1, n2 * 2, h + 1)

for s in range(1,74):
    if f(7,s,1):
        print(s)

#Фан факт: Если написано, что ход "НЕУДАЧНЫЙ" это значит хотя бы 1, а не любой ход из выборки
