import random
import turtle

SCREEN_SIZE = 700
MAX_RADIUS = 75
t = turtle.Pen()


def dandelion():
    stem()
    seedpuff()


def stem():
    t.speed("normal")
    t.penup()
    t.setpos(random.randint(MAX_RADIUS, SCREEN_SIZE - MAX_RADIUS), 0)
    t.setheading(90)
    t.pencolor("#00FF00")
    t.pendown()
    t.forward(random.randint(MAX_RADIUS * 2, SCREEN_SIZE - MAX_RADIUS))


def seedpuff():
    t.speed("fastest")
    t.pencolor("#000000")
    t.pendown()
    radius = random.randint(int(MAX_RADIUS / 3), MAX_RADIUS)
    for heading in range(90, 90 - 360, -15):
        t.setheading(heading)
        t.forward(radius)
        t.backward(radius)


def doit():
    t.clear()
    for i in range(8):
        dandelion()
    turtle.ontimer(doit, 3000)


turtle.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
turtle.setworldcoordinates(0, 0, SCREEN_SIZE, SCREEN_SIZE)
t.hideturtle()

doit()
