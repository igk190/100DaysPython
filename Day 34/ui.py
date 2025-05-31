from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:  # PascalCase, Day 17

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.geometry("340x450")

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0, padx=20, pady=10)
        
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, background="white") 
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.canvas_text = self.canvas.create_text(150,125,text="Some Question Text", fill=THEME_COLOR, font=FONT )

        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img,highlightthickness=0)
        self.true_button.grid(column=0, row=2, pady=20)     

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0)
        self.false_button.grid(column=1, row=2, pady=20)   


        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_text, text=q_text)


""" Learnings
1. Label() only affects the widget’s internal config (e.g. padding inside the label).
grid() controls widget placement, incl. spacing between widgets.
2. Makes more sense to use Button class instead of Label for things we want to interact with.

"""


