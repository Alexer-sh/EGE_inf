import turtle as t
t.screensize(5000,5000)
t.left(90)
t.speed(5000)
k=20
t.down()
for i in range(12):
    t.right(60)
    t.forward(1*k)
    t.right(60)
    t.forward(1*k)
    t.right(270)

t.up()
for x in range(-5, 10):
    for y in range(-10, 10):
        t.goto(x*k,y*k)
        t.dot('red')
while True:
    a=0