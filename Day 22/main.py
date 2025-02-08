from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0)) 
l_paddle = Paddle((-350, 0))
    
screen.listen()
screen.onkey(l_paddle.up, "W") 
screen.onkey(l_paddle.down, "S")

game_is_on = True

while game_is_on:
    screen.update()





screen.exitonclick()

""" Learnings

1. Teacher used paddle.goto(xcor,ycor). I'm not yet sure why when we can first
reset the heading, then just use fowrward and backward.

2. When you turn off the animation, you manually have to update the screen and refresh it every time. 
Instead of doing it each time after keystrokes, we can let the game itself do this.
"""