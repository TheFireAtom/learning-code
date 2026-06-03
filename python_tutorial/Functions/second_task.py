from turtle import *

def triangle(dir, a):
    color("green")
    if dir == 'dn':
        begin_fill()
        fd(a)
        lt(60)
        bk(a)
        lt(60)
        fd(a)
        rt(120)
        end_fill()
    elif dir == 'up':
        begin_fill()
        fd(a)
        rt(60)
        bk(a)
        rt(60)
        fd(a)
        lt(120)
        end_fill()
    elif dir == 'rt':
        begin_fill()
        rt(30)
        fd(a)
        lt(60)
        bk(a)
        lt(60)
        fd(a)
        end_fill()
    elif dir == 'lt':
        begin_fill()
        lt(30)
        bk(a)
        rt(60)
        fd(a)
        rt(60)
        bk(a)
        end_fill()
    done()

triangle('lt', 90)
