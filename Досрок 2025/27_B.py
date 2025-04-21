#Тут 2 кластера разделённые по принципу y V 0
import math

f=open("27_B_21425.txt").readlines()
ax=[]
ay=[]
bx=[]
by=[]
cx=[]
cy=[]
for t in f:
    t=t.replace(',','.')
    x,y=map(float,t.split())
    if x<1.0:
        ax.append(x)
        ay.append(y)
    elif y>0:
        bx.append(x)
        by.append(y)
    else:
        cx.append(x)
        cy.append(y)
mn_d=10000000000000000000
x1=[]
y1=[]
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
x1.append(mn_x)
y1.append(mn_y)
mn_d=10000000000000000000
mn_x=0
mn_y=0
for i in range(len(bx)):
    sm=0
    for j in range(len(bx)):
        sm+=math.sqrt((bx[i]-bx[j])**2 + (by[i]-by[j])**2)
    if sm< mn_d:
      mn_d=sm
      mn_y=by[i]
      mn_x=bx[i]
x1.append(mn_x)
y1.append(mn_y)
print(mn_x,mn_y)
mn_d=10000000000000000000
mn_x=0
mn_y=0
for i in range(len(cx)):
    sm=0
    for j in range(len(cx)):
        sm+=math.sqrt((cx[i]-cx[j])**2 + (cy[i]-cy[j])**2)
    if sm< mn_d:
      mn_d=sm
      mn_y=cy[i]
      mn_x=cx[i]
x1.append(mn_x)
y1.append(mn_y)
print(mn_x,mn_y)
print(sum(x1)/3 * 10000,sum(y1)/3 * 10000)

#Ваще то же самое, но только больше и дольше


