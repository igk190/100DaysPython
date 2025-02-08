from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.setheading(90)
        self.resizemode("user")
        self.penup()
        self.shapesize(1, 5)
        self.color("white") 
        self.goto(coordinates)


    def up(self):
        self.fd(20)

    def down(self):
        self.bk(20)


