from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:  # PascalCase, Day 17

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.canvas = Canvas(width=400, height=500, highlightthickness=0, background="white") 
        self.canvas.grid(column=1, row=1)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.canvas.create_image(100,100, image=self.true_img)
        self.canvas.create_image(100,100, image=self.false_img)
        

        self.window.mainloop()

# scoreboard label
# canvas background with text
# 2 buttons
