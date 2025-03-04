from turtle import Turtle

class StateTracker(Turtle):

    def __init__(self):
        super().__init__()
        self.all_guessed_states = []
        self.color("black")
        self.penup()
        self.hideturtle()
        self.states_guessed_title = f"{len(self.all_guessed_states)}/50 States Correct"

    def write_state(self, state, x, y):
        self.goto(x, y)
        self.pendown()
        self.write(state, True, align="center")
        self.penup()
    
    def update_state(self, state):
        self.all_guessed_states.append(state)
        self.states_guessed_title = f"{len(self.all_guessed_states)}/50 States Correct"

    