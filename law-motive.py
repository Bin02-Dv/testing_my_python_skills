import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Motivational Message for Kausar")


pen = turtle.Turtle()
pen.hideturtle()
pen.color("lightgreen")
pen.penup()
pen.speed(0)

font = ("Courier", 18, "bold")

message = (
    "Dear Kausar, \n"
    "In a world full of noise, be the voice of justice.\n"
    "Let the law be your sword, and truth your shield. \n"
    "Your brilliance is needed in courtrooms and beyound. \n \n"
    "Stand tall. Speak bold. Think wise.\n"
    "Because you're not just learning law...\n"
    "You're becoming the light in the dark.. ⚖️"
)

def type_writer(msg, x, y, delay=0.05):
    pen.goto(x, y)
    for char in msg:
        if char == "\n":
            y -= 30
            x = -300 
            pen.goto(x, y)
        else:
            pen.write(char, font=font)
            x += 12
            pen.goto(x, y)
        time.sleep(delay)

type_writer(message, -300, 180)

pen.goto(0, -100)
pen.color("red")
pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)
pen.end_fill()

pen.color("white")
pen.penup()
pen.goto(0, -280)
pen.write("— With Love & Pride 💼", align="center", font=("Courier", 14, "italic"))

turtle.done()