#Новая итерация безумия в виде регулярных выражений (помянем)

from re import finditer
s=open("24 (2).txt").readlines()
reg = r'[ABC]+' #Тут мы берём 3 символа и ищем их вождение в строку >= 1 раза
mx=0
for x in finditer(reg,s[0]):
    print(x.group())
    mx = max(mx,len(x.group()))
print(mx)
