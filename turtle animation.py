from turtle import *
import colorsys

speed(0)
bgcolor('black')
pensize(2)
h=0.5

for i in range(410):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    fd(i)
    lt(100*5)
    lt(10)

done()