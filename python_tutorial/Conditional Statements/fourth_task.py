from turtle import *

month = None
season = None
running = True

while running:
    month = int(input("Type month: "))
    if month == 12 or month == 1 or month == 2:
        season = "Winter"
        running = False
    elif month in range(3, 5+1):
        season = "Spring"
        running = False
    elif month in range(6, 8+1):
        season = "Summer"
        running = False
    elif month in range(9, 11+1):
        season = "Autumn"
        running = False
    else:
        print("Oops, you typed non-existend month. Try again.")

print("Your season is:", season)