from turtle import *

hunter = Turtle()
steven = Turtle()
taylor = Turtle()

mode("standard")

colormode(255)

screensize(1000, 1000, "sky blue")

title("A Pretty Little Scene")

hunter.shape("turtle")
steven.shape("turtle")
taylor.shape("turtle")

def draw_sun(x, y, line, fill):
    hunter.penup()
    hunter.goto(x, y)
    hunter.pendown()
    hunter.hideturtle()

    hunter.color(line, fill)
    
    begin_fill()
    for i in range(36):
        hunter.forward(100)
        hunter.left(100)
    end_fill()
    hunter.showturtle()
speed(100)

def draw_star(x, y, points, line, fill):
    steven.penup()
    steven.goto(x, y)
    steven.pendown()
    steven.hideturtle()

    turn = 180 - (360 / points)

    steven.color(line, fill)

    begin_fill()
    for i in range(points):
        steven.forward(200)
        steven.left(turn)
    end_fill()
    steven.showturtle()
speed(100)

def draw_flower(x, y, line, fill):
    taylor.penup()
    taylor.goto(x, y)
    taylor.pendown()
    taylor.hideturtle()

    taylor.color(line, fill)

    begin_fill()
    for i in range(36):
        taylor.forward(100)
        taylor.right(110)
        taylor.forward(100)
        taylor.right(110)
    end_fill()
    taylor.showturtle()
speed(100)

def draw_stem(x, y, line):
    hunter.penup()
    hunter.goto(x, y)
    hunter.pendown()
    hunter.pensize(10)
    hunter.resizemode("auto")

    hunter.color(line)

    while True:
        hunter.left(90)
        hunter.back(200)
        hunter.right(90)
        hunter.forward(10)
        hunter.left(90)
        hunter.forward(200)
        hunter.left(90)
        hunter.forward(10)
        if abs(pos()) < 1:
            break
speed(100)

def draw_cloud(x, y, line, fill):
    taylor.penup()
    taylor.goto(x, y)
    taylor.pendown()
    taylor.pensize(15)
    taylor.resizemode("auto")

    steven.penup()
    steven.goto(x, y)
    steven.pendown()
    steven.pensize(15)
    steven.resizemode("auto")

    taylor.color(line, fill)
    steven.color(line, fill)

    begin_fill()
    while True:
        taylor.forward(200)
        taylor.right(90)
        taylor.forward(100)
        taylor.right(90)
        taylor.forward(200)
        taylor.right(90)
        taylor.forward(100)

        steven.forward(200)
        steven.right(90)
        steven.forward(100)
        steven.right(90)
        steven.forward(200)
        steven.right(90)
        steven.forward(100)
        if abs(pos()) < 1:
            break
    end_fill()
speed(100)   

def forward(distance):
    while distance > 0:
        if turtle.distance(0,0) > 600:
            angle = turtle.towards(0,0)
            turtle.setheading(angle)
        turtle.forward(1)
        distance = distance - 1

hunter.ondrag(goto)

onkeypress(draw_cloud, "Up")

draw_sun(400, 200, (255, 165, 0), "yellow")

draw_flower(-350, 0, "orchid", "gold")
draw_flower(400, 0, "salmon", "gray")

draw_star(0, -200, 50, "red", "black")
draw_star(200, -200, 50, "indigo", "pink")
draw_star(-200, -200, 50, "magenta", "violet")

draw_stem(-300, -200, "green")
draw_stem(450, -200, "green")

draw_stem(100, -300, "green")
draw_stem(300, -500, "green")
draw_stem(-100, -300, "green")


draw_cloud(-400, 300, "gray", "white")
draw_cloud(0, 200, "gray", "white")

done()
exitonclick()

