from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.reset_player()


    def move_up(self):
        self.fd(MOVE_DISTANCE)
    
    def reset_player(self):
        self.goto(STARTING_POSITION)

    def reached_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True

# Learnings: if repeating code that's in a method, call the method in init directly.