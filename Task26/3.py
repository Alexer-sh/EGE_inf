"""
Для перевозки партии грузов различной массы выделен грузовик, но его грузоподъёмность ограничена, поэтому перевезти сразу все грузы не удастся.
Грузы массой от 200 до 210кг грузят в первую очередь, гарантируется, что все такие грузы поместятся. На оставшееся после этого место стараются взять как можно больше грузов.
Если это можно сделать несколькими способами, выбирают тот способ, при котором самый большой из выбранных грузов имеет наибольшую массу. Если и при этом условии возможно несколько вариантов, выбирается тот, при котором наибольшую массу имеет второй по величине груз, и так далее. Известны количество грузов, масса каждого из них и грузоподъёмность грузовика. Необходимо определить количество и общую массу грузов, которые будут вывезены при погрузке по вышеописанным правилам.
Первая строка входного файла содержит два целых числа: N— общее количество грузов и M— грузоподъёмность грузовика в кг. Каждая из следующих N строк содержит одно целое число— массу груза в кг.
В ответе запишите два целых числа: сначала максимально возможное количество грузов, затем их общую массу.
"""
#Задача по сути аналогичная задаче из 1.py
f = open("26.3.txt").readlines()
n,s=list(map(int,f[0].split()))
a=[]
c=0
s1=s
for t in range(1,len(f)):
    b=int(f[t])
    if b>=200 and b<=210:
        s-=b
        c+=1
    else:
        a.append(int(f[t]))
a.sort()
d=0
while s>0:
    s-=a[d]
    c+=1
    d+=1
s+=a[d]
c-=1
d-=1
print(c)
s+=a[d]
mx=a[d]
j=len(a)-1
while 1!=0:
    if s-a[j]>=0:
        mx=a[j]
        break
    j-=1
print(s1-s+mx)
#Крч, надо внимательно смотреть на идексы, по которым мы добавляем/убавляем элементы

