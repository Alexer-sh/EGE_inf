f=open("24.txt")
r=f.readlines()
n=int(r[0])
A=[]
B=[]
for i in range(1,n):
    st=r[i].split()
    if st[0]=="A":
        A.append(int(st[1]))
    else:
        B.append(int(st[1]))
A.sort(reverse = True)
B.sort(reverse = True)
c=0
sm=0
for i in range(len(B)):
    for j in range(len(A)):
        if abs(B[i]-A[j])<=15:
            c+=1
            sm+=B[i]+A[j]
            del A[j]
            break
print(c,sm)