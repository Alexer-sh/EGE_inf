from re import finditer
s=open("24_21908.txt").readlines()
num = r'(([1-9]|[ABCD])([0-9]|[ABCD])*)'

mx=max([x.group() for x in finditer(num,s[0])],key=len)
print(len(mx),mx)
#Это просто работает, как-то...