import turtle
import time

class Node:
    def __init__(self, key, x, y):
        self.key = key
        self.left = None
        self.right = None
        self.x = x
        self.y = y

def draw_node(t, key, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(20)
    t.penup()
    t.goto(x - 7, y - 7)
    t.write(str(key), font=("Arial", 12, "bold"))

def draw_line(t, x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

def insert(t, node, key, x, y, dx):
    if node is None:
        draw_node(t, key, x, y)
        return Node(key, x, y)
    
    if key < node.key:
        draw_line(t, node.x, node.y - 20, x - dx, y - 60)
        node.left = insert(t, node.left, key, x - dx, y - 60, dx / 2)
    else:
        draw_line(t, node.x, node.y - 20, x + dx, y - 60)
        node.right = insert(t, node.right, key, x + dx, y - 60, dx / 2)
    
    return node

screen = turtle.Screen()
screen.title("BST Animation")
t = turtle.Turtle()
t.speed(0)

root = None
positions = [50, 30, 70, 20, 40, 60, 80]
for value in positions:
    root = insert(t, root, value, 0, 200, 80)
    time.sleep(1)

t.hideturtle()
screen.mainloop()