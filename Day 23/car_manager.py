from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(COLORS[randint(0,5)])
        new_car.goto(300, randint(-250, 250))
        # new_car.setheading(180)
        self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

        
    
   

        
        
""" Learnings
1. You don't need to reset heading if you stretch the turtle in the width. Or?
"""