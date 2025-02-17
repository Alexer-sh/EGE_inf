
f=[0]*101
f[3]=3
c=0
for i in range(4,101):
    if i % 2 ==0:
        f[i]=2*i+f[i-1]
    else:
        f[i]= i*i +f[i-2]
for i in range(3,101):
    if f[i]%3==0:
        c+=1
print(c)