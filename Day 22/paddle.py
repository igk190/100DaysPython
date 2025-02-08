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
        self.coordinates = coordinates
        self.set_position()

    def set_position(self):
        self.goto(self.coordinates)
        # self.set_paddle_coordinates()

    # def set_paddle_coordinates(self, xcor, ycor):
    #     self.goto(xcor, ycor)

    def up(self):
        self.fd(20)

    def down(self):
        self.bk(20)


