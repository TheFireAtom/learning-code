from turtle import *

colors = ["red", "blue", "violet", "yellow"]

# firts method 

for angle in range(0, 360, 90):
    if angle == 0:
        pencolor(colors[0])
    elif angle == 90:
        pencolor(colors[1])
    elif angle == 180:
        pencolor(colors[2])
    elif angle == 270:
        pencolor(colors[3])
    seth(angle)
    fd(100)

# second method

for angle, color in zip(range(0, 360, 90), colors):
    pencolor(color)
    seth(angle)
    fd(100)

done()



