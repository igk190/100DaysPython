from turtle import Turtle

class StateTracker(Turtle):

    def __init__(self):
        super().__init__()
        self.states_guessed_correctly = 0
        self.color("black")
        self.penup()
        self.states_guessed_title = f"{self.states_guessed_correctly} States Correct"
        # self.refresh()

    def write_state(self, state, x, y):
        self.goto(x, y)
        self.pendown()
        self.write(state, True, align="center")

    
    # def refresh(self):
    #     random_x = random.randint(-280, 280)
    #     random_y = random.randint(-280, 280)
    #     self.goto(random_x, random_y)