from turtle import Turtle, Screen
import random

colors = [
    "black", "gray", "silver", "red", "maroon", "yellow", "olive",
    "lime", "green", "aqua", "teal", "blue", "navy", "fuchsia", "purple",
    "orange", "brown", "pink", "gold", "cyan", "magenta"
]

pensize = 1
step = 10

def random_color():
    color_choice = random.choice(colors)
    sketch.color(color_choice)

def pen_up():
    sketch.penup()

def pen_down():
    sketch.pendown()

def move_right():
    sketch.forward(step)

def move_left():
    sketch.backward(step)

def rotate_left():
    sketch.left(20)

def rotate_right():
    sketch.right(20)

def clear_screen():
    sketch.clear()
    show_text()

def show_text():
    global pensize
    sketch.color("black")
    pensize = 1
    sketch.pensize(pensize)
    sketch.penup()
    sketch.goto(x=0, y= -250)
    sketch.write("'u' Pen Up    /    'd' Pen down", font=("Arial", 16, "normal"), align="center")
    sketch.goto(x=0, y= -280)
    sketch.write("Press 'c' to clear screen.", font=("Arial", 16, "normal"), align="center")
    sketch.goto(x=0, y= 0)
    sketch.showturtle()
    sketch.pendown()

def increase_width():
    global pensize
    if sketch.pensize() != 0:
        pensize += 1
        sketch.pensize(pensize)

def decrease_width():
    global pensize
    if sketch.pensize() != 0:
        pensize -= 1
        sketch.pensize(pensize)

screen = Screen()
screen.bgcolor('white')
screen.title("Etch a Sketch")

sketch = Turtle()
sketch.hideturtle()
sketch.shape("classic")
sketch.shapesize(0.8)
sketch.color("black")
sketch.pensize(pensize)
show_text()

screen.onkey(pen_up, 'u')
screen.onkey(pen_down, 'd')
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")
screen.onkey(rotate_left, "Up")
screen.onkey(rotate_right, "Down")
screen.onkey(clear_screen, "c")
screen.onkey(increase_width, "i")
screen.onkey(decrease_width, "o")
screen.onkey(random_color, "r")

screen.listen()

screen.mainloop()



