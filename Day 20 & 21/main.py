from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

start_y = 0

for i in range(0, 3):
    square = Turtle("square")
    square.color("white")
    square.goto(start_y,0)
    start_y -= 20













screen.exitonclick()