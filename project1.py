import turtle as t
def rectangle (hor, vert, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(hor)
        t.right(90)
        t.forward(vert)
        t.right(90)
    t.end_fill()
    t.penup()


t.penup()
t.speed('slow')
t.bgcolor('dodger blue')

# ступни
t.goto(-100,-150)
rectangle(50,20,'blue')
t.goto(-30,-150)
rectangle(50,20,'blue')

#legs
t.goto(-25,-50)
rectangle(15,100,'grey')
t.goto(-55,-50)
rectangle(-15,100,'grey')

#body
t.goto(-90,100)
rectangle(100,150,'red')

#arms
t.goto(-150,70)
rectangle(60,15,'grey')
t.goto(-150,110)
rectangle(15,40,'grey')

t.goto(10,70)
rectangle(60,15,'grey')
t.goto(55,110)
rectangle(15,40,'grey')

#neck
t.goto(-50,120)
rectangle(15,20,'grey')

#head
t.goto(-85,170)
rectangle(80,50,'red')