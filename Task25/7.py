"""
Среди натуральных чисел, не превышающих 1013, найдите все числа, соответствующие маске 12?345?67089?,
делящиеся на 206 без остатка. В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
а во втором столбце – соответствующие им результаты деления этих чисел на 206.
"""
#from fnmatch import *
#for n in range(10**12-8,10**13+1,206):
#    if fnmatch(str(n),"12?345?67089?"):
#        print(n,n//206)
#Это не самый эффективный способ решения

for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            st="12"+str(i)+"345"+str(j)+"67089"+str(k)
            t=int(st)
            if t%206==0:
                print(st, t//206)