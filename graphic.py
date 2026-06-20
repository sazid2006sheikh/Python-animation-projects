from turtle import *
import colorsys 
import turtle 

speed(0)
bgcolor('black')
pensize(2)
h=0.5
# for square shape
turtle.shape("arrow")
turtle.right(20)
turtle.forward(40)

for i in range(200):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    rt(10)

    for j in range(5):
     fd(i)
     rt(20*5)
    rt(120)

done()
