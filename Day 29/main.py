from tkinter import * 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #



def save():

    f = open("data.txt", "a+")
    
    website_value = website_entry.get()
    email_value = email_entry.get()
    password_value = password_entry.get()

    f.write(f'\n{website_value} | {email_value} | {password_value}')
    content = f.readlines()
    print(content)
    f.close()

    website_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    password_entry.delete(0, 'end')






# save that data into file called data.text
# take all 3 with space in between and pipe symbol or staticmethod
# on press button, trigger function that saves info in data.txt File
# append file on new line underneath previous entry

# once press add, all of info except email cleared OUTSIDE
# look at delete finctoion entirely from an entry

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
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_user_label = Label(text="E-mail/Username:", fg="black", bg="white")
email_user_label.grid(column=0, row=2)

email_entry = Entry(width=35, bg="white", fg="black", highlightthickness=0, borderwidth=1)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "hello@email.com")

password_label = Label(text="Password:", fg="black", bg="white")
password_label.grid(column=0, row=3)
password_entry = Entry(width=18, bg="white", fg="black", highlightthickness=0, borderwidth=1)
password_entry.grid(column=1, row=3)
generate_pw_btn = Button(text="Generate password", highlightbackground="white", anchor="e")
generate_pw_btn.grid(column=2, row=3)

add_btn = Button(text="Add to MyPass", width=32, highlightbackground="white", command=save)
add_btn.grid(column=1, row=4, columnspan=2)





window.mainloop()