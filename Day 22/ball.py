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




"""Learnings
1. dot only stamps a dot on the screen, shape("circle) makes turtle itself a circle. 
"""