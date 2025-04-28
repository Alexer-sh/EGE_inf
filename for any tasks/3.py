f=open("9.3.txt").readlines()
d=0
mx1=0.0
for t in f:
    a=list(map(float,t.split(';')))
    mx=max(a)
    if mx>mx1:
        mx1=mx
        print(mx)
        print(a)
for t in f:
    a=list(map(float,t.split(';')))
    d+=a.count(mx1)
print(d)