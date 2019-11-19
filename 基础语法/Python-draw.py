#导入全部函数，以减少代码量
from turtle import *
setup(400,300,300,200)
penup()
fd(-250)
pendown()
pensize(25)
pencolor("black")
seth(-40)
for i in range(4):
    circle(40,80)
    circle(-40,80)
circle(40,40)
fd(40)
circle(16,180)
fd(40*2/3)
done()