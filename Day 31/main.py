from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk() 
window.title("Flashy")
window.geometry("900x700")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526,highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 262, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=wrong_img, highlightthickness=0)
cross_button.grid(column=0, row=1,)












window.mainloop()