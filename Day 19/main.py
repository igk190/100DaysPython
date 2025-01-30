import turtle
from turtle import Turtle, Screen

from PIL.Image import blend

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color.")
colors = ["red","orange","yellow","green","blue","purple"] # correspond to colors turtle will recognize

colors_list_length = len(colors)
turtle_list = []

tim = turtle_list.append(Turtle(shape="turtle"))
orange_turtle = turtle_list.append(Turtle(shape="turtle"))
yellow_turtle = turtle_list.append(Turtle(shape="turtle"))
green_turtle = turtle_list.append(Turtle(shape="turtle"))
blue_turtle = turtle_list.append(Turtle(shape="turtle"))
purple_turtle = turtle_list.append(Turtle(shape="turtle"))

start_x = -230
start_y = 90
color_index = 0

for racer in turtle_list:
    racer.penup()
    racer.goto(start_x, start_y)
    start_y -= 30
    racer.color(colors[color_index])
    color_index += 1




screen.exitonclick()

""" Learnings
1. Either use left or setheading to a new number.
2. There is a clear message for the turtle, and for the screen. Clearscreen deletes everyting.
Clear only deletes the drawing.
3. Tried to create instances using a for loop with range(colors_list_length -1). Got a KeyError.
4. Okay, guess I could've created a for loop with range to create all the turtles at once anyway.
"""