f=open("9.5.txt").readlines()
d=0
for t in f:
    a=list(map(int,t.split(';')))
    a=sorted(a)
    if a[0] + a[1] < a[2] or a[0] + a[1] < a[3]:
        d+=1
        print(a)
print(d)