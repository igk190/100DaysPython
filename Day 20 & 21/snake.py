from turtle import Turtle
STEP_SIZE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.heading = 0


    def create_snake(self):
        start_x = 0
        for i in range(0, 3):   
            square = Turtle("square")
            square.color("white")
            square.penup()
            square.goto(start_x, 0)
            start_x -= 20
            self.segments.append(square)
    

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # index 2, 1, 0
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            self.segments[0].forward(STEP_SIZE)
        
    def up(self):
        self.segments[0].setheading(90)
    def down(self):
        self.segments[0].setheading(270)
    def left(self):
        self.segments[0].setheading(180)
    def right(self):
        self.segments[0].setheading(0)


""" Learnings
1. We only move the head of the snake. The other segments follow. 
2.     def up(self):
        self.segments = self.segments[0].setheading(90)
    --> we don't need to reassign self.segments, as setheading(90)
    directly modifies the first element. See Learnings #1. 
"""