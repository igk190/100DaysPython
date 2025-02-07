from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong Game")

x_pos = 350 
y_pos = 0

right_paddle = Turtle()
right_paddle.shape("square")
right_paddle.setheading(90)
right_paddle.resizemode("user")
right_paddle.penup()
right_paddle.shapesize(1, 5) # original 20 x 20
right_paddle.color("white")
right_paddle.goto(x_pos, y_pos)

        
# print(right_paddle.position())


def up():
    right_paddle.fd(20)

def down():
    right_paddle.bk(20)
    

screen.listen()
screen.onkey(up, "Up") 
screen.onkey(down, "Down")





screen.exitonclick()