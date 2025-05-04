f = open("9.txt").readlines()
c=0
for t in f:
    a=list(map(int,t.split(';')))
    fl=True
    for i in range(1,7):
        if a[i] >a[i-1]:
            fl=False
    if fl and ((max(a)+min(a))/2 >(sum(a)-(max(a)+min(a)))/5):
        print(a)
        c+=1
print(c)