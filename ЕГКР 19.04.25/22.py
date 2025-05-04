c=0
def f(n,fl1,fl2):
    if n==89:
        if fl1 and fl2:
            global c
            c+=1
            print("12345678")
            return
        else:
            return
    if n>89:
        return
    if n == 40:
        fl1=True
    if n == 72:
        fl2=True
    if n==56:
        return
    f(n+3,fl1,fl2)
    f(n + 7, fl1, fl2)
    f(n *3, fl1, fl2)


f(12,False,False)
print(c)

