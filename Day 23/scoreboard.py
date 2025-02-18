from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 275)
        self.write("Score: ", align="center", font=FONT)
        self.goto(-210, 275)
        self.write(self.score, align="center", font=FONT)

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)

