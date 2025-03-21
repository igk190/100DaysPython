from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 45), bg=YELLOW)
timer_title.grid(column=1, row=0)

start_btn = Button(text="Start", highlightbackground=YELLOW)
start_btn.grid(column=0, row=3)

checkmark = "✔"
checkmark_label = Label(text=checkmark, fg=GREEN, font=(FONT_NAME, 30), bg=YELLOW)
checkmark_label.grid(column=1, row=3)

stop_btn = Button(text="Stop", highlightbackground=YELLOW)
stop_btn.grid(column=2, row=3)




# canvas_timer = Canvas(width=20, height=10, bg=YELLOW, highlightthickness=0)
# canvas_timer.create_text(100, 130, text="Timer", fill=GREEN, font=(FONT_NAME, 30, "bold"), fg=GREEN)
# canvas_timer.grid(column=1, row=0)






window.mainloop()


"""Learnings

1. If you set the bg color of a label to match that of the window, you use fg to color the text itself."""