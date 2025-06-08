f=open("26_20910.txt").readlines()
n = 99907  # строки
m = 6662  # столбцы
a = [[0] * m for _ in range(n)]
b=[99907]*6662
del f[0]
c=0
e=0
for t in f:
    i,j=list(map(int,t.split()))
    a[i][j]=1
    b[j]=min(i,b[j])
print(b)

