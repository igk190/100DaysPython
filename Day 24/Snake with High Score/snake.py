from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP_SIZE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    
    def add_segment(self, position):
            square = Turtle("square")
            square.color("white")
            square.penup()
            square.goto(position)
            self.segments.append(square)
    
    def reset(self):
        for square in self.segments:
            square.goto(0,700)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # index 2, 1, 0
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(STEP_SIZE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


""" Learnings
1. We only move the head of the snake. The other segments follow. 

2.     def up(self):
        self.segments = self.segments[0].setheading(90)
    --> we don't need to reassign self.segments, as setheading(90)
    directly modifies the first element. See Learnings #1. 

3. Now it makes sense: we need one snake body, to which we add elements.
    Only the first segment determines the direction. The rest just follows
    the path of segments before it.

4. It makes sense to add an attribute that refers to segments[0]. Makes 
    the code shorter/cleaner. (I wrote self.segments[0].setheading(direction))

5. Check how you name attributes and functions when using modules! "Heading" is a Turtle method.
"""