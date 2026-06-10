from turtle import *

cnt = 6

def turtle_move(dir, rg):
    if dir == "w":
        seth(90)
        fd(rg)
    elif dir == "d":
        seth(0)
        fd(rg)
    elif dir == "a":
        seth(180)
        fd(rg)
    elif dir == "s":
        seth(270)
        fd(rg)

for _ in range(cnt):
    turtle_move(input("Введите направление (wasd): "), 100)
    update()


