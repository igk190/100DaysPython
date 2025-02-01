from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

start_x = 0
segments = []

for i in range(0, 3):   # all of this should go into Snake class
    square = Turtle("square")
    square.color("white")
    square.penup()
    square.goto(start_x,0)
    start_x -= 20
    segments.append(square)

game_is_on = True  # main.py should end up looking like this
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    
    for seg_num in range(len(segments) - 1, 0, -1):  # index 2, 1, 0
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)




#why in the previous one she used a for loop to create all of them at once?
# And here they are separately initialized? Okay she does this later in the video

screen.exitonclick()