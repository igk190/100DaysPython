from turtle import Turtle, Screen
import random


is_race_on = False

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

if user_bet:
    is_race_on = True

while is_race_on: # prevent while loop from starting up while user is still betting

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've chose {user_bet} and won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've chose {user_bet} and lost. The {winning_color} turtle is the winner.")

        rand_distance = random.randint(0, 10)  # inclusive, includes 10
        turtle.forward(rand_distance) # edit this

screen.exitonclick()

""" Learnings

1. Either use left or setheading to a new number.

2. There is a clear message for the turtle, and for the screen. Clearscreen deletes everyting.
Clear only deletes the drawing.

3. Tried to create instances using a for loop with range(colors_list_length -1). Got a KeyError.

4. Okay, guess I could've created a for loop with range to create all the turtles at once anyway.

5. Angela used turtle_index in the range(0,6) which excluded 6 to give each turtle their y coordinate.
All y_positions were placed in a list. Then, she used tim.goto(... y=y_positions[turtle_index])
I'm not adjusting my program with this solution just yet. We don't need the turtles named, we can
make them move through loops.
"""