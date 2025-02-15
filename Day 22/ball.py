from turtle import Turtle
from random import randint, choice

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(randint(1,90))
        self.x_coordinate = 0
        self.speed = 0

    def move(self):
        # print("ball is moving...")
        self.fd(10)
    
    def bounce_off_wall(self):
        if self.ycor() > 300 or self.ycor() < -300:
            self.setheading(360 - self.heading())

    def reset(self, x_coordinate):
        self.goto(0,0)
        self.setheading(0) 

        if x_coordinate > 400:
            self.setheading(randint(91, 180)) # go left

        else:
            new_direction = choice([randint(270, 360), randint(0, 90)]) # go right
            self.setheading(new_direction)

    def increase_speed(self):
        self.speed += 0.5 
      
    def rumble_screen(self):
        if (self.heading() >= 0 and self.heading() <= 90) or (self.heading() >= 270 and self.heading() <= 360): # heading pointing right
            # self.setheading(0) 
            self.setheading(choice([randint(0,70), randint(300,360)]))
        elif (self.heading() > 90 and self.heading() < 270): # heading pointing left
            # self.setheading(0) 
            self.setheading(randint(130, 240))



"""Learnings
1. dot only stamps a dot on the screen, shape("circle) makes turtle itself a circle. 

2. Here the teacher also adjusts the coordinates instead of resetting the heading, and then moving in that direction.

3. We're mirroring the bounce of the ball on the y-axis. To get the value we reset heading with, we take the full
circle, and subtract the current heading. 

4. random choice returns a random element from a sequence (str, range, list, tuple). So, make sure to enter a sequence.
random.choice([randint(0, 90), randint(1,5)])
"""