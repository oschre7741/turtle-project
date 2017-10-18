from turtle import *

def draw_star(x, y, points, line, fill):
    penup()
    goto(x, y)
    pendown()

    turn = 180 - (360 / points)

    color(line, fill)

    begin_fill()
    for i in range(points):
        forward(200)
        left(turn)
    end_fill()

speed(200)

draw_star(0, 0, 102, "black", "red")
draw_star(0, 200, 72, "blue", "green")
draw_star(0, -200, 72, "magenta", "violet")
draw_star(-200,0, 72, "indigo", "pink")
draw_star(200, 0, 72, "purple", "gray")
draw_star(200, 200, 72, "blue", "green")
draw_star(200, -200, 72, "magenta", "violet")
draw_star(-200, 200, 72, "indigo", "pink")
draw_star(-200, -200, 72, "purple", "gray")

done()
