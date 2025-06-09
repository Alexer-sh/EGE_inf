f=open("24_20813.txt").readline()
from re import *
num=r'([789][0987]*|0)'
reg=rf'{num}([-*]{num})+'
m=max([x.group() for x in finditer(reg,f)], key =len)
print(m)
print(len(m))
