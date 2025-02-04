from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)

    def updateScore(self):
        self.score += 1 

    def writeScore(self):
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)
        
    


