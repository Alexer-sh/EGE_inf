f = open("9.txt").readlines()
c=0
for t in f:
    a=list(map(int,t.split(';')))
    if len(set(a))==5:
        a1=a
        a1.sort()
        if a1[0]+a1[1]+a1[2]>=a1[3]+a1[4]:
            c+=1
            print(a)
print(c)