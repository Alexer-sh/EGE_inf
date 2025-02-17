#Магическая программа на адекватном языке, а не дичь на кумире, ура!
import turtle as t
t.left(90)
t.speed(1000)
k=10
t.down()
for i in range(3):
    t.forward(7*k)
    t.right(90)
t.forward(10*k)
for i in range(3):
    t.left(90)
    t.forward(6*k)
t.up()
for x in range(-3, 8):
    for y in range(-6, 8):
        t.goto(x*k,y*k)
        t.dot('red')
while True:
    a=0