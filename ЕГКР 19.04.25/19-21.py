def f(x,h):
    if (h==5 or h==3) and x>=128:
        return 1
    elif h==5 and x<128:
        return 0
    elif h<5 and x>=128:
        return 0
    else:
        if h%2!=0:  #Ход Пети
            return f(x+2,h+1) and f(x+5,h+1) and f(x*2,h+1)
        else:       #Ход Вани
            return f(x + 2, h + 1) or f(x + 5, h + 1) or f(x * 2, h + 1)
for x in range(1,127):
    if f(x,1)==1:
        print(x)
        break
