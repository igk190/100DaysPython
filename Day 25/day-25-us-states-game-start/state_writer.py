from turtle import Turtle

class StateWriter(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        # self.refresh()

    def write_state(self, x, y, state):
        self.goto(x, y)
        self.pendown()
        self.write(state, True, align="center")
    
    # def refresh(self):
    #     random_x = random.randint(-280, 280)
    #     random_y = random.randint(-280, 280)
    #     self.goto(random_x, random_y)