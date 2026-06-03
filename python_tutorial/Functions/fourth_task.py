from turtle import *

def triangle(a):
    color("green")
    begin_fill()
    fd(a)
    lt(60)
    bk(a)
    lt(60)
    fd(a)
    rt(120)
    end_fill()

def sgoto(x, y):
    up()
    width(2)
    goto(x, y)

def rectangle(a, b):
    color("brown")
    begin_fill()
    fd(a)
    rt(90)
    fd(b)
    rt(90)
    fd(a)
    rt(90)
    fd(b)
    end_fill()

rectangle(25, 100)
sgoto(25, -45)
triangle(45)
sgoto(25, -90)
triangle(45)

done()
