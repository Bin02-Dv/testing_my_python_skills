import turtle
import colorsys

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
hue = 0

for i in range(360):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(color)
    t.forward(i * 0.5)
    t.left(59)
    hue += 0.002
    
t.hideturtle()
turtle.done()