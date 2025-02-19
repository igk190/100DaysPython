from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.high_score = 0
        self.hideturtle()
        self.goto(0, 280)
        self.writeScore()
 
    def writeScore(self): # finally write all scores to screen
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score # update high score if needed
        self.score = 0  # reset score to zero
        self.writeScore()

    def increaseScore(self):
        self.score += 1   
        self.writeScore()


        
    


