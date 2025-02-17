
import turtle as t
t.left(90)
t.speed(1000)
k=10
t.down()
for i in range(10):
    t.forward(22*k)
    t.right(90)
    t.forward(18 * k)
    t.right(90)
t.up()
t.forward(1*k)
t.right(90)
t.forward(1*k)
t.left(90)
t.down()
for i in range(10):
    t.forward(72 * k)
    t.right(90)
    t.forward(79 * k)
    t.right(90)
t.up()
for x in range( 0, 100):
    for y in range(-20, 30):
        t.goto(x*k,y*k)
        t.dot('red')
while True:
    a=0