import turtle as t
t.left(90)
t.speed(1000)
k=10
t.down()
t.right(30)
for i in range(3):
    t.right(150)
    t.forward(6*k)
    t.right(30)
    t.forward(12*k)
t.up()
for x in range(-10, 10):
    for y in range(-20, 0):
        t.goto(x*k,y*k)
        t.dot('red')
while True:
    a=0