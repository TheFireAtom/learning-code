from turtle import *
import random

tree_coef = 100
bgcolor("black")
how_many_trees = int(input("write how many trees do you want to draw: "))

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
    width(2)
    goto(x, y)

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

# moon
sgoto(300, 250)
begin_fill()
color("white")
for m in range(72):
    fd(5)
    lt(5)
end_fill()
# sgoto(0, 0)

def random_star(count):
    random_star_coef_x = random.randint(-4, 4)
    random_star_coef_y = random.randint(-4, 4)
    sgoto(100* random_star_coef_x, 250 * random_star_coef_y)
    begin_fill()
    color("white")
    if len()
    for m in range(72):
        fd(5)
        lt(5)
    end_fill()

already_exist = []

def random_tree():
    if len(already_exist) >= 9:
        print("All tree positions are full!!!")
        return

    random_tree = random.randint(-4, 4)

    while random_tree in already_exist:
        random_tree = random.randint(-4, 4)

    already_exist.append(random_tree)
    print(f"Drawing unique tree at position: {random_tree}")

    new_tree_coef = 25
    color("brown")
    sgoto(tree_coef*random_tree, random_tree*new_tree_coef)
    rectangle(25, 100)
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

# random trees
for _ in range(1, how_many_trees):
    random_tree()
    
# ground 
sgoto(-500, 0)
color("chocolate4")
begin_fill()
rectangle(1000, 500)
end_fill()

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


