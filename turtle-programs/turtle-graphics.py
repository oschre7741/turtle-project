from turtle import *

colormode(255)

hunter = Turtle()
steven = Turtle()
taylor = Turtle()

hunter.shape("turtle")

steven.shape("turtle")

taylor.shape("turtle")

def draw_sun(x, y, line, fill):
    hunter.penup()
    hunter.goto(x, y)
    hunter.pendown()

    hunter.color(line, fill)
    
    begin_fill()
    for i in range(36):
        hunter.forward(75)
        hunter.left(100)
    end_fill()


def draw_star(x, y, points, line, fill):
    steven.penup()
    steven.goto(x, y)
    steven.pendown()

    turn = 180 - (360 / points)

    steven.color(line, fill)

    begin_fill()
    for i in range(points):
        steven.forward(200)
        steven.left(turn)
    end_fill()

def draw_flower(x, y, line, fill):
    taylor.penup()
    taylor.goto(x, y)
    taylor.pendown()

    taylor.color(line, fill)

    begin_fill()
    for i in range(36):
        taylor.forward(100)
        taylor.right(125)
        taylor.forward(100)
        taylor.right(125)
    end_fill()
    

speed(1000)

draw_sun(400, 200, (214, 110, 12), "yellow")
draw_flower(-300, 0, "red", "gold")
draw_flower(300, 0, "magenta", "gray")
draw_star(0, -200, 102, "black", "red")
draw_star(100, -200, 72, "indigo", "pink")
draw_star(-100, -200, 72, "magenta", "violet")

done()

