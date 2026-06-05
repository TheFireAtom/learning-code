from turtle import *
import random

tree_coef = 100
bgcolor("black")
how_many_trees = int(input("Write how many trees do you want to draw: "))
how_many_stars = int(input("Write how many stars do you want to draw: "))
trees_already_exist = []
stars_already_exist = []

def triangle(dir, a):
    if dir == 'dn':
        begin_fill()
        fd(a)
        lt(60)
        bk(a)
        lt(60)
        fd(a)
        rt(120)
        rt(90)
        lt(90)
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
        rt(90)
        end_fill()
    elif dir == 'lt':
        begin_fill()
        lt(30)
        bk(a)
        rt(60)
        fd(a)
        rt(60)
        bk(a)
        lt(90)
        end_fill()

def sgoto(x, y):
    up()
    width(1)
    goto(x, y)
    down()

def rectangle(a, b):
    begin_fill()
    fd(a)
    rt(90)
    fd(b)
    rt(90)
    fd(a)
    rt(90)
    fd(b)
    rt(90)
    end_fill()

def draw_star(size):
    color("white")
    begin_fill()
    for _ in range(5):
        fd(size)
        rt(144)
    end_fill()

# Logic for spawning random stars
def random_star():
    if len(stars_already_exist) >= how_many_stars:
        print("All stars positions are full!!!")
        return
    
    random_star = random.randint(0, 20) 

    while random_star in stars_already_exist:
        random_star = random.randint(0, 20)

    stars_already_exist.append(random_star)
    print(f"Drawing unique star at position: {random_star}")

    random_star_coef_x = random.randint(-20, 20)
    random_star_coef_y = random.randint(2, 10)
    random_star_main_coef = 25
    sgoto(random_star_main_coef * random_star_coef_x, random_star_main_coef * random_star_coef_y)
    
    draw_star(20)

    # for _ in range(72):
    #     fd(1)
    #     lt(5)
    # end_fill()

# logic for spawing random trees
def random_tree():
    if len(trees_already_exist) >= how_many_trees:
        print("All tree positions are full!!!")
        return

    random_tree = random.randint(-4, 4)

    while random_tree in trees_already_exist:
        random_tree = random.randint(-4, 4)

    trees_already_exist.append(random_tree)
    print(f"Drawing unique tree at position: {random_tree}")

    new_tree_coef = 25
    color("brown")
    sgoto(tree_coef*random_tree, random_tree*new_tree_coef)
    rectangle(25, 100)
    color("green")
    sgoto(25 + tree_coef*random_tree, random_tree*new_tree_coef)
    triangle('rt', 45)
    sgoto(25 + tree_coef*random_tree, random_tree*new_tree_coef-45)
    triangle('rt', 45)
    sgoto(tree_coef*random_tree, random_tree*new_tree_coef)
    triangle('lt', 45)
    sgoto(tree_coef*random_tree, random_tree*new_tree_coef-45)
    triangle('lt', 45)
    sgoto(tree_coef*random_tree - 10, new_tree_coef*random_tree)
    triangle('up', 45)

# moon
sgoto(300, 250)
begin_fill()
color("white")
for m in range(72):
    fd(5)
    lt(5)
end_fill()
# sgoto(0, 0)

# ground 
sgoto(-500, 0)
color("chocolate4")
begin_fill()
rectangle(1000, 500)
end_fill()

# random trees
for _ in range(how_many_trees):
    random_tree()

# random stars
for _ in range(how_many_stars):
    random_star()

done()

# # first tree
# sgoto(0, 0)
# color("brown")
# rectangle(25, 100)
# sgoto(25, 0)
# triangle('rt', 45)
# sgoto(25, -45)
# triangle('rt', 45)
# sgoto(0, 0)
# triangle('lt', 45)
# sgoto(0, -45)
# triangle('lt', 45)
# sgoto(-10, 0)
# triangle('up', 45)

# # second tree
# color("brown")
# sgoto(25 + 75, 0)
# rectangle(25, 100)
# sgoto(25 + tree_coef, 0)
# triangle('rt', 45)
# sgoto(25 + tree_coef, -45)
# triangle('rt', 45)
# sgoto(0 + tree_coef, 0)
# triangle('lt', 45)
# sgoto(0 + tree_coef, -45)
# triangle('lt', 45)
# sgoto(-10 + tree_coef, 0)
# triangle('up', 45)

# # thrid tree
# color("brown")
# sgoto(25 - tree_coef - 25, 0)
# rectangle(25, 100)
# sgoto(25 - tree_coef, 0)
# triangle('rt', 45)
# sgoto(25 - tree_coef, -45)
# triangle('rt', 45)
# sgoto(0 - tree_coef, 0)
# triangle('lt', 45)
# sgoto(0 - tree_coef, -45)
# triangle('lt', 45)
# sgoto(-10 - tree_coef, 0)
# triangle('up', 45)


