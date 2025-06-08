import math

f=open("27_A_20911.txt").readlines()
ax=[]
ay=[]
bx=[]
by=[]
for t in f:
    t=t.replace(",",".")
    x,y=list(map(float,t.split()))
    if y>0:
        ax.append(x)
        ay.append(y)
    else:
        bx.append(x)
        by.append(y)
mn_d=100000000000000
mn_x=[]
mn_y=[]
x=0
y=0
for i in range(len(ax)):
    sm=0
    for j in range(len(ax)):
        sm+=math.sqrt((ax[i]-ax[j])**2+(ay[i]-ay[j])**2)
    if sm<mn_d:
        mn_d=sm
        x=ax[i]
        y=ay[i]
mn_x.append(x)
mn_y.append(y)
mn_d = 100000000000000
x = 0
y = 0
for i in range(len(bx)):
    sm = 0
    for j in range(len(bx)):
        sm += math.sqrt((bx[i] - bx[j]) ** 2 + (by[i] - by[j]) ** 2)
    if sm < mn_d:
        mn_d = sm
        x = bx[i]
        y = by[i]
mn_x.append(x)
mn_y.append(y)
print(sum(mn_x)/2 * 10_000,sum(mn_y)/2 * 10_000)
