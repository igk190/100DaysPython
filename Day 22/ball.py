from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(random.randint(1,90))

    def move(self):
        print("ball is moving...")
        self.fd(10)
    
    def detect_wall_collision(self):
        if self.ycor() > 305 or self.ycor() < -305:
            self.setheading(360 - self.heading())



"""Learnings
1. dot only stamps a dot on the screen, shape("circle) makes turtle itself a circle. 

2. Here the teacher also adjusts the coordinates instead of resetting the heading, and then moving in that direction.
"""