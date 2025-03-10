F = [0]*10009
F[0]=0
F[1]=1
F[2]=2
F[3]=3
F[4]=4
F[5]=5
for i in range(6,10000):
    if i%8==0:
        F[i]=i+F[i//2-3]
for i in range(9999-3,5,-1):
    if i%8!=0:
        F[i]=i+F[i+4]
print(F)
print(max(F))