from turtle import Turtle



class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()


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
            self.segments[0].forward(20)
        

