import turtle
turtle.screensize(600,400,'blue')
turtle.pensize(1)
turtle.pencolor('purple')
angle = 0
while angle!=360:
    turtle.setheading(float(angle))
    for i in range(0,6):
        turtle.fd(50)
        turtle.left(60)
    angle+=2
turtle.invisable()
turtle.done()