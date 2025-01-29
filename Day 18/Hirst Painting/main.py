from email.utils import collapse_rfc2231_value
from turtle import *
import random

# Turtle setup
timmy = Turtle()
screen = timmy.getscreen()
timmy.shape("turtle")
timmy.color("pink")
timmy.speed("fastest")
timmy.hideturtle()
colormode(255)

def get_random_color():
    color_list = [
        (239, 191, 115), (228, 158, 71), (43, 20, 35), (162, 75, 54),
        (130, 156, 87), (58, 31, 20), (246, 237, 196), (218, 101, 70),
        (237, 232, 236), (111, 78, 85), (101, 48, 39),
        (102, 42, 46), (78, 67, 40), (166, 157, 165),
    ]
    n = random.randint(0, len(color_list))
    random_color = color_list[n-1] # minus one, or the index could be out of range!
    print("this is the random color", random_color, n)

    return random_color

x = -250
y = -250

def draw_row_of_dots():
    global x
    global y
    counter = 0
    for _ in range(10):  # stop is omitted, you need only 9
        timmy.penup()
        timmy.setx(x)
        timmy.sety(y)
        # timmy.pendown()
        # timmy.pencolor(get_random_color())
        # timmy.begin_fill()
        timmy.dot(20, get_random_color()) # from solution, forgot about 2nd param
        timmy.end_fill()
        # timmy.penup()
        x += 50
        counter += 1
        print(counter, timmy.position())
    y += 50
    x += -500  # because after the last one, you still added 50 (you need 450 + 50)
    print(y)

for _ in range(10):
    draw_row_of_dots()
    print("We are here: ", x, y)
    timmy.goto(x, y)

screen.exitonclick()

""" Learnings
 1. Instead of using a functon to get a random rgb value, use random.choice(color_list) that takes the whole list.
2. you didn't read the documentation: .dot takes 2 parameters, where the second one is the color.
3. I don't touch timmy.setheading() followed by move. Instead, I set the coordinates with timmy.setx and timmy.sety.
4. Another approach is: Don't lift the pen in-between drawing the dots. This can help draw out/visualize the path.
Afterward, you can get rid of the path.
5. Apparently for dots to be drawn, we don't need to put the pen up and down.
"""