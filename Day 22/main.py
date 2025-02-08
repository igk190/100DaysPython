from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.tracer(0)

right_paddle = Turtle()
right_paddle.shape("square")
right_paddle.setheading(90)
right_paddle.resizemode("user")
right_paddle.penup()
right_paddle.shapesize(1, 5) # original 20 x 20
right_paddle.color("white") # gets initialized at center
right_paddle.goto(350, 0)
screen.update()

def up():
    right_paddle.fd(20)


def down():
    right_paddle.bk(20)

    
screen.listen()
screen.onkey(up, "Up") 
screen.onkey(down, "Down")

game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()

""" Learnings
1. Teacher used paddle.goto(xcor,ycor). I'm not yet sure why when we can first
reset the heading, then just use fowrward and backward.
2. When you turn off the animation, you manually have to update the screen and refresh it every time. 
"""