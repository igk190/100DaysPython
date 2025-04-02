from tkinter import *
import pandas as pd
from random import randint

BACKGROUND_COLOR = "#B1DDC6"
PT_FONT = ("Arial", 40, "italic")
EN_FONT = ("Arial", 60, "bold")

# ------------------------ Read CSV ------------------------
df = pd.read_csv('data/pt_en.csv')
print(df["PT"].values[0])
print(df["EN"].values[0])


# ------------------------ Get random PT word ------------------------
def cant_recall():
    canvas.itemconfig(pt_word, fill="green", text=df["PT"].values[randint(0, 1000)])

def correct_guess():
    canvas.itemconfig(pt_word, fill="green", text=df["PT"].values[randint(0, 1000)])




window = Tk() 
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526,highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 262, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

pt_text = canvas.create_text(400, 150, text="Portuguese", fill="black", font=PT_FONT)
pt_word = canvas.create_text(400, 263, text=df["PT"].values[randint(0, 1000)], fill="black", font=EN_FONT)

wrong_icon = PhotoImage(file="images/wrong.png")
cross_button = Button(image=wrong_icon, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=cant_recall)
cross_button.grid(column=0, row=1)

right_icon = PhotoImage(file="images/right.png")
right_button = Button(image=right_icon, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=correct_guess)
right_button.grid(column=1, row=1)














window.mainloop()

""" Learnings

1. I assumed Labels could be added to Canvas. But since I wanted to place text on the canvas, I should've
searched for 'Tkinter add text to canvas.' That would've led me to canvas.create_text.
Canvas allows us to layer/draw items and overlap them on top of each other. 

2. To center images on the canvas, take half of the canvas width and height.
Positions of text on the canvas are relative to the size canvas too.

"""