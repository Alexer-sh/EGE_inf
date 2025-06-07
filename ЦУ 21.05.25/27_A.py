import math

f=open("zadacha-27a-e0528399-7be9-4159-a5ad-8ca041b31c45.txt").readlines()
ax=[]
ay=[]
bx=[]
by=[]
for t in f:
    t=t.replace(',','.')
    x,y=map(float,t.split(';'))
    if x>0:
        ax.append(x)
        ay.append(y)
    else:
        bx.append(x)
        by.append(y)
mn_d=10000000000000000000
mn_d1=10000000000000000000
mn_x=0
mn_y=0
mn_x1=0
mn_y1=0
for i in range(len(ax)):
    sm=0
    sm1=0
    for j in range(len(ax)):
        sm+=math.sqrt((ax[i]-ax[j])**2 + (ay[i]-ay[j])**2)
        sm1+=abs(ax[i]-ax[j])+abs(ay[i]-ay[j])
    if sm< mn_d:
      mn_d=sm
      mn_y=ay[i]
      mn_x=ax[i]
    if sm1<mn_d1:
        mn_d1 = sm1
        mn_y1 = ay[i]
        mn_x1 = ax[i]
print(mn_x,mn_y)
print(mn_x1,mn_y1)
mn_d=10000000000000000000
mn_x1=0
mn_y1=0
for i in range(len(bx)):
    sm=0
    for j in range(len(bx)):
        sm+=math.sqrt((bx[i]-bx[j])**2 + (by[i]-by[j])**2)
    if sm< mn_d:
      mn_d=sm
      mn_y1=by[i]
      mn_x1=bx[i]
print(mn_x1,mn_y1)
print((mn_x+mn_x1)/2 *10000, (mn_y+mn_y1)/2 *10000)


