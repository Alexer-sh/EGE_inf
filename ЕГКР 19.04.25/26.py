a=[[0]*1000001]*1000001   #i - student, j - task
f=open("26_21719.txt").readlines()
mx=0
for t in f:
    i,j = list(map(int,t.split()))
    a[i][j]=1
for i in range(1000001):
    mx1=0
    for j in range(100000-1):
        if a[i][j]==0 and a[i][j+1]==1:
            mx1+=1
    if mx1>mx:
        mx=mx1
    print(mx1,i)
