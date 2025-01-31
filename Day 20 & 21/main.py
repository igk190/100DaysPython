from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

start_x = 0

for i in range(0, 3):
    square = Turtle("square")
    square.color("white")
    square.goto(start_x,0)
    start_x -= 20











#why in the previous one she used a for loop to create all of them at once?
# And here they are separately initialized? Okay she does this later in the video

screen.exitonclick()