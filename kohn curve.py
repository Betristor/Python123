import turtle
def kohn_curve(size,n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            kohn_curve(size/3,n-1)

def main():
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.begin_fill()
    turtle.color('red')
    level = 4
    kohn_curve(400,level)
    turtle.right(120)
    kohn_curve(400,level)
    turtle.right(120)
    kohn_curve(400,level)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.done()

main()