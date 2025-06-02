from tkinter import *
import pandas as pd
from random import randint
BACKGROUND_COLOR = "#B1DDC6"
PT_FONT = ("Arial", 40, "italic")
EN_FONT = ("Arial", 60, "bold")

# ------------------------ Read CSV ------------------------
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv('data/pt_en.csv')
print(df)
current_card_index = randint(0, len(df)-1)

# ------------------------ Show answer (flip card) ------------------------
def show_answer():
    canvas.itemconfig(canvas_image, image=card_back) 
    canvas.itemconfig(lang_text, text="English translation", fill="white")
    canvas.itemconfig(word_to_learn, fill="white", text=df["EN"].values[current_card_index])

# ------------------------ Next card (get random PT word) ------------------------
def next_card():
    global df
    global current_card_index

    print("df before reset", df)
    df = df.reset_index(drop=True) # reset index, drop the original one
    print("df after reset", df)
    
    current_card_index = randint(0, len(df)-1) # reset random int, so show_answer can access it
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(lang_text, text="Portuguese", fill="green")
    canvas.itemconfig(word_to_learn, fill="black", text=df["PT"].values[current_card_index]) # 
    window.after(3000, show_answer)

# ------------------------ Remove from list ------------------------
def remove_from_list():
    global df
    df = df.drop(df.index[current_card_index]) # remove current row
    df.to_csv("data/words_to_learn.csv", index=False) # update CSV with new df/words to learn
    next_card()


window = Tk() 
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 262, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

lang_text = canvas.create_text(400, 150, text="Portuguese", fill="green", font=PT_FONT)
word_to_learn = canvas.create_text(400, 263, text=df["PT"].values[current_card_index], fill="black", font=EN_FONT)
window.after(3000, show_answer)

wrong_icon = PhotoImage(file="images/wrong.png")
cross_button = Button(image=wrong_icon, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
cross_button.grid(column=0, row=1)

right_icon = PhotoImage(file="images/right.png")
right_button = Button(image=right_icon, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=remove_from_list)
right_button.grid(column=1, row=1)



window.mainloop()

""" Learnings

1. I assumed Labels could be added to Canvas. But since I wanted to place text on the canvas, I should've
searched for 'Tkinter add text to canvas.' That would've led me to canvas.create_text.
Canvas allows us to layer/draw items and overlap them on top of each other. 

2. To center images on the canvas, take half of the canvas width and height.
Positions of text on the canvas are relative to the size canvas too.

3. To not get out of bounds index, take 1 off len().

4. When you set index to false in df.to_csv("words_to_learn.csv", index=False), pandas doesn't save the indices.
It only includes actual words and translations.

"""