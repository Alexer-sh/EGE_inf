import turtle as t
t.screensize(5000,5000)
t.left(90)
t.speed(5000)
k=20
t.down()
for i in range(3):
    t.forward(27*k)
    t.right(90)
    t.forward(12*k)
    t.right(90)
t.up()
t.forward(4 * k)
t.right(90)
t.forward(6 * k)
t.left(90)
t.down()
for i in range(4):
    t.forward(83*k)
    t.right(90)
    t.forward(77*k)
    t.right(90)
t.up()
for x in range(-0,50):
    for y in range(-5,30):
        t.goto(x*k,y*k)
        t.dot('red')
while 1!=0:
    a=0

    #Стороны прямоугольников идут на +1 от своей длины
    #Фан факт