"""
Текстовый файл 24-196.txt содержит строку из заглавных латинских букв X, Y и Z, всего не
более чем из 106 символов. Определите максимальное количество идущих подряд пар символов
ZX или ZY.
"""

from re import finditer
s=open("24 (1).txt").readlines()
reg = r'(PQ|QS)+' #Тут мы ищем комбинации подряд идущих выбранных пар
mx=0
print([x.group() for x in finditer(reg,s[0])])