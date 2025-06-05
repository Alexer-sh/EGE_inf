import turtle as t
t.screensize(5000,5000)
t.left(90)
t.speed(5000)
k=20
t.down()
t.right(90)
for i in range(7):
    t.right(45)
    t.forward(11*k)
    t.right(45)
t.up()
for x in range(-10, 25):
    for y in range(-15, 10):
        t.goto(x*k,y*k)
        t.dot('red')
while True:
    a=0