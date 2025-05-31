from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:  # PascalCase, Day 17

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.geometry("340x450")

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0, padx=20, pady=10)
        
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, background="white") 
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.canvas_text = self.canvas.create_text(150,125,text="blabla", fill="black", font=FONT )

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")

        self.true_label = Label(self.window, image=self.true_img)
        self.true_label.grid(column=0, row=2, pady=20)
        self.false_label = Label(self.window, image=self.false_img)
        self.false_label.grid(column=1, row=2, pady=20)

        

        self.window.mainloop()

""" Learnings
1. Label() only affects the widget’s internal config (e.g. padding inside the label).
grid() controls widget placement, incl. spacing between widgets.


"""


