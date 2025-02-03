
class Snake:
    def __init__(self, shape="square", color="white", x=0, y=0, penup=True):
        self.shape = shape
        self.color = color
        self.x = x
        self.y = y
        self.penup = penup

    def create_snake(self):
        start_x = 0

for i in range(0, 3):   # all of this should go into Snake class
    square = Turtle("square")
    square.color("white")
    square.penup()
    square.goto(start_x,0)
    start_x -= 20
    segments.append(square)

    # def update_x_y(self):
    #     #do sth
    
    # def move(self):
        # do sth

#     segments = []

# for seg_num in range(len(segments) - 1, 0, -1):  # index 2, 1, 0
#     new_x = segments[seg_num -1].xcor()
#     new_y = segments[seg_num -1].ycor()
#     segments[seg_num].goto(new_x, new_y)
# segments[0].forward(20)
    

