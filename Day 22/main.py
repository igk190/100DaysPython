from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0)) 
l_paddle = Paddle((-350, 0))
ball = Ball()
    
screen.listen()

screen.onkey(l_paddle.up, "w") 
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up") 
screen.onkey(r_paddle.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    # time.sleep(0.1)
    ball.move()
    print(ball.position)
    ball.bounce_off_wall()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.setheading(180- ball.heading())



screen.exitonclick()

""" Learnings

1. Teacher used paddle.goto(xcor,ycor). I'm not yet sure why when we can first
reset the heading, then just use fowrward and backward.

2. When you turn off the animation, you manually have to update the screen and refresh it every time. 
Instead of doing it each time after keystrokes, we can let the game itself do this

3. If we want Paddle Class to take extra arguments, add position here to be passed over to self.addgoto(coordinates)

4. Reminder: methods always have a first attribute called self. 

5. 'W' or 'w' matters when defining which key to listen to. Capital w works only with shift + W. 
Shift key event is also pressed.
"""