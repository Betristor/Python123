import turtle
turtle.screensize(600,400,'white')
turtle.pensize(1)
turtle.pencolor('blue')
angle = 0
d = 1
while angle!=360:
    turtle.seth(angle)
    for i in range(6):
        turtle.fd(d)
        turtle.left(60)
    angle += 12
    d += 2
turtle.done()