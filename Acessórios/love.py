import turtle
import math

tur = turtle.Turtle()
tur.speed(0)
tur.color("red")
turtle.bgcolor("white")


def heart(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
    return x, y

tur.penup()
for i in range(15):
    tur.goto(0, 0)
    tur.pendown()
    for n in range(0, 100, 2):
        x, y = heart(n / 10)
        tur.goto(x * i, y * i)
    tur.penup()

tur.hideturtle()
turtle.done()
