from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 4
CHECKMARK = "✔"
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps

    window.after_cancel(timer)
    reps = 0
    checkmark_label.config(text="")
    # timer_text.itemconfig(text="00:00")
    canvas.itemconfig(timer_text, text="00:00")
    timer_title.config(text="Timer")
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps 
    print(f"Reps start timer before incr: {reps}")
    reps += 1
    print(f"Reps start itmer afte rincr: {reps}")

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_title.config(text="Break", fg=RED)
        countdown(long_break_sec)    
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_title.config(text="Break", fg=PINK)
    else:
        countdown(work_sec) 
        timer_title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count): # take input in form of the num to countdown by
    global reps

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10: 
        count_sec = f"0{str(count_sec)}"

    if count > -1 : # higher than zero
        global timer
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, countdown, count - 1) # after 1K ms, call countdown, and pass in a num
    else: #   if/once count == 0:
        start_timer()
        print(f"Reps: {reps}")
        if reps % 2 == 0:
            checkmark_label.config(text=CHECKMARK * (reps // 2))
            print(f"Reps: {reps}")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 45), bg=YELLOW)
timer_title.grid(column=1, row=0)

start_btn = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_btn.grid(column=0, row=3)


checkmark_label = Label(fg=GREEN, font=(FONT_NAME, 30), bg=YELLOW)
checkmark_label.grid(column=1, row=3)

reset_btn = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_btn.grid(column=2, row=3)



# canvas_timer = Canvas(width=20, height=10, bg=YELLOW, highlightthickness=0)
# canvas_timer.create_text(100, 130, text="Timer", fill=GREEN, font=(FONT_NAME, 30, "bold"), fg=GREEN)
# canvas_timer.grid(column=1, row=0)






window.mainloop()


"""Learnings

1. If you set the bg color of a label to match that of the window, you use fg to color the text itself.

2. Highlightthickness=0 doesn't remove border/background from button. 
highlightbackground=YELLOW does. 

3. changing text on label. title_label.config(text="...") For a canvas: canvas.itemconfig
Then you pass in item you want to configure, and the thing you want to change
canvas.itemconfig(timer_text, text=count)

4. We can also floor the reps to a whole number instead of a float.
work_session = math.floor(reps/2)

"""