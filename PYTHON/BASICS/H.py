import math
import turtle

def hearta(k):
    return 12*math.sin(k)-5*math.sin(2*k)-2*math.sin(3*k)-math.sin(4*k)

def heartb(k):
    return 12*math.cos(k)-5*math.cos(2*k)-2*math.cos(3*k)-math.cos(4*k)

turtle.speed(0)
turtle.bgcolor("black")
turtle.color("red")
turtle.penup()

for k in range(1000):
    x = hearta(k * 0.01)
    y = heartb(k * 0.01)
    turtle.goto(x * 20, y * 20)
    turtle.pendown()

turtle.done()