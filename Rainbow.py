import turtle
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])
def draw_circle(size, angle, shift):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size, angle+1, shift)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(8)

draw_circle(30, 0, 1)


