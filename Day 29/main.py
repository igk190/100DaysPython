from tkinter import * 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=250, height=250,highlightthickness=0, bg="white")
logo = PhotoImage(file="logo.png")
canvas.create_image(125, 125, image=logo)
# timer_text = canvas.create_text(100, 100)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", fg="black", bg="white")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35, bg="white", fg="black", highlightthickness=0, borderwidth=1)
website_entry.grid(column=1, row=1, columnspan=1)

email_user_label = Label(text="E-mail/Username:", fg="black", bg="white")
email_user_label.grid(column=0, row=2)

email_entry = Entry(width=35, bg="white", fg="black", highlightthickness=0, borderwidth=1)
email_entry.grid(column=1, row=2)

password_label = Label(text="Password:", fg="black", bg="white")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21, bg="white", fg="black", highlightthickness=0, borderwidth=1)
password_entry.grid(column=1, row=3, columnspan=1)
generate_pw_btn = Button(text="Generate password", highlightbackground="white", anchor="e")
generate_pw_btn.grid(column=2, row=3)

add_btn = Button(text="Add to MyPass", width=36, highlightbackground="white")
add_btn.grid(column=1, row=4, columnspan=1)





window.mainloop()