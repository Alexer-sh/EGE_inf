import turtle as t
t.screensize(5000,5000)
t.left(90)
t.speed(1000)
k=50
t.down()
for i in range(7):
    t.forward(10*k)
    t.right(120)
t.up()
for x in range(0, 10):
    for y in range(-3, 12):
        t.goto(x*k,y*k)
        t.dot('red')
while True:
    a=0