import turtle
import colorsys
import time

turtle.colormode(1)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.hideturtle()

h = 0.0

for i in range(10):
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    
    r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
    pen.color((r, g, b), (r, g, b))
    
    pen.begin_fill()
    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.left(120)
    pen.circle(-90, 200)
    pen.forward(180)
    
    h += 0.02
    time.sleep(0.1)
    
colors = ["red", "pink", "white", "hot pink"]
pen.penup()
pen.goto(0, -180)
pen.pendown()

for i in range(10):
    pen.clear()
    pen.color(colors[i % len(colors)])
    pen.write("I Love you", align="center", font=("Arial", 24, "bold"))
    time.sleep(0.4)

turtle.done()