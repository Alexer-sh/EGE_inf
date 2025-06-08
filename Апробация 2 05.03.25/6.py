import turtle as t
t.screensize(5000,5000)
k=20
t.speed(10000)
t.left(90)
t.down()
for i in range(7):
    t.forward(27*k)
    t.right(90)
    t.forward(30*k)
    t.right(90)
t.up()
t.forward(3*k)
t.right(90)
t.forward(6*k)
t.left(90)
t.down()
for i in range(9):
    t.forward(77*k)
    t.right(90)
    t.forward(66*k)
    t.right(90)
t.up()
for x in range(0,50):
    for y in range(-20,40):
        t.goto(x*k,y*k)
        t.dot('red')
while 1!=0:
    a=0