#Тут 2 кластера разделённые по принципу y V 0
import math

f=open("27_A_21425.txt").readlines()
ax=[]
ay=[]
bx=[]
by=[]
for t in f:
    t=t.replace(',','.')
    x,y=map(float,t.split())
    if y>0:
        ax.append(x)
        ay.append(y)
    else:
        bx.append(x)
        by.append(y)
mn_d=10000000000000000000
mn_x=0
mn_y=0
for i in range(len(ax)):
    sm=0
    for j in range(len(ax)):
        sm+=math.sqrt((ax[i]-ax[j])**2 + (ay[i]-ay[j])**2)
    if sm< mn_d:
      mn_d=sm
      mn_y=ay[i]
      mn_x=ax[i]
print(mn_x,mn_y)
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

#Несложно, если читать задание и думать


