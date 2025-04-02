from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
PT_FONT = ("Arial", 40, "italic")
EN_FONT = ("Arial", 60, "bold")

window = Tk() 
window.title("Flashy")
window.geometry("900x700")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526,highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 262, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

canvas.create_text(400, 150, text="Portuguese Word", fill="black", font=PT_FONT)
canvas.create_text(400, 263, text="English word", fill="black", font=EN_FONT)


# pt_text = Label(text="Portuguese word", fg="black", bg="white", font=PT_FONT)
# pt_text.grid(column=0, row=0)
# en_text = Label(text="English word", fg="black", bg="white", font=EN_FONT)
# en_text.grid(column=0, row=1)

wrong_icon = PhotoImage(file="images/wrong.png")
cross_button = Button(image=wrong_icon, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
cross_button.grid(column=0, row=1,)

right_icon = PhotoImage(file="images/right.png")
right_button = Button(image=right_icon, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
right_button.grid(column=1, row=1,)












window.mainloop()