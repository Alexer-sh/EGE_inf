import math

f = open("9 (4).txt")
r =f.readlines()
mx=0.0
for t in r:
    a=list(map(float,t.split(';')))
    if math.sqrt(a[0]**2+a[1]**2)>mx:
        mx=math.sqrt(a[0]**2+a[1]**2)
print(mx)
