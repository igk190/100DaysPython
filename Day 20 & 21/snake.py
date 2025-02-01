class Snake:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }


    def move(self):
        """ Moves the snake."""
        # do sth
            for seg_num in range(len(segments) - 1, 0, -1):  # index 2, 1, 0
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
       