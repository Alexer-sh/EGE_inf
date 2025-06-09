import math

f=open("27_A_20816.txt").readlines()
ax=[]
ay=[]
bx=[]
by=[]
for t in f:
    x,y=list(map(float,t.split()))
    if x>0:
        ax.append(x)
        ay.append(y)
    else:
        bx.append(x)
        by.append(y)
mn_d=100000000000000000
x1=0
y1=0
mn_x=[]
mn_y=[]
for i in range(len(ax)):
    sm = 0
    for j in range(len(ay)):
        sm+=math.sqrt((ax[i]-ax[j])**2+ (ay[i]-ay[j])**2)
    if sm<mn_d:
        mn_d=sm
        x1=ax[i]
        y1=ay[i]
print(x1,y1)
mn_x.append(x1)
mn_y.append(y1)
mn_d=100000000000000000
for i in range(len(bx)):
    sm = 0
    for j in range(len(by)):
        sm+=math.sqrt((bx[i]-bx[j])**2+ (by[i]-by[j])**2)
    if sm<mn_d:
        mn_d=sm
        x1=bx[i]
        y1=by[i]
print(x1,y1)
mn_x.append(x1)
mn_y.append(y1)
print(sum(mn_x)/len(mn_x)*10_000,sum(mn_y)/len(mn_y)*10_000)