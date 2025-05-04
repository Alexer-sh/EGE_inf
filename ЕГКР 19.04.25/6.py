import turtle as t
t.screensize(5000,5000)
t.left(90)
t.speed(5000)
k=20
t.down()
for i in range(2):
    t.forward(28*k)
    t.right(90)
    t.forward(18*k)
    t.right(90)
t.up()
t.forward(14*k)
t.right(90)
t.forward(10*k)
t.left(90)
t.down()
for i in range(2):
    t.forward(30*k)
    t.right(90)
    t.forward(7*k)
    t.right(90)
t.up()
for x in range(0, 50):
    for y in range(0, 50):
        t.goto(x*k,y*k)
        t.dot('red')
while True:
    a=0