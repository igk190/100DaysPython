from tkinter import * 
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for letter in range(randint(8, 10))]
    numbers_list = [choice(numbers) for number in range(randint(2, 4))]
    symbols_list = [choice(symbols) for symbol in range(randint(2, 4))]

    password_list = letters_list + numbers_list + symbols_list
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password) 


# ---------------------------- FIND PASSWORD ------------------------------- #    
def find_password():
    with open("data.json", "r") as f:
        data = json.load(f)
        # print(data["Ebay"])
        website_value = website_entry.get()
        print(data[website_value])
        # get whatever input user typed in entry field
        # use that as key to return
        # if exists


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website_value = website_entry.get()
    email_value = email_entry.get()
    password_value = password_entry.get()

    new_data = { 
        website_value: {
        "email": email_value,
        "password": password_value
        }
    }

    if website_value == "" or password_value == "": 
        messagebox.showerror(title="Ups", message="Please fill out all fields.")
    else:
        is_ok = messagebox.askokcancel(title=website_value, message=f"The details you entered:\n{email_value}\nPassword: {password_value}. \nIs it okay to save?")
        if is_ok:
            try:
                with open("data.json", "r") as f:
                    data = json.load(f) # Read old data
            except FileNotFoundError:
                with open("data.json", "w") as f:
                   json.dump(new_data, f, indent=4) # save/write data with NEW data, if it caught an error theres nothing from line 44 inside data
            else:
                data.update(new_data) # update old data with new data
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)
            finally:
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


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

website_entry = Entry(width=18, bg="white", fg="black", highlightthickness=0, borderwidth=1)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

search_btn = Button(width=10, text="Search", highlightbackground="white", command=find_password)
search_btn.grid(column=2, row=1, columnspan=1, sticky="W")

email_user_label = Label(text="E-mail/Username:", fg="black", bg="white")
email_user_label.grid(column=0, row=2)

email_entry = Entry(width=35, bg="white", fg="black", highlightthickness=0, borderwidth=1)
email_entry.grid(column=1, row=2, columnspan=2, sticky="")
email_entry.insert(0, "hello@email.com")

password_label = Label(text="Password:", fg="black", bg="white")
password_label.grid(column=0, row=3)
password_entry = Entry(width=18, bg="white", fg="black", highlightthickness=0, borderwidth=1)
password_entry.grid(column=1, row=3, columnspan=1)
generate_pw_btn = Button(text="Generate password", highlightbackground="white", anchor="e", command=generate_password)
generate_pw_btn.grid(column=2, row=3)

add_btn = Button(text="Add to MyPass", width=32, highlightbackground="white", command=save)
add_btn.grid(column=1, row=4, columnspan=2)





window.mainloop()


""" Learnings

1. with open(data.txt, "a") as data file: closes the file automatically for you! 

2. Read the documentation, the param reads "message" not "text."

3. I was stuck on an error I created. The code file is set up as such:
If there is no file, create one, and write the new_data to it.
If there IS a file, update, then dump (write) it. The error occurred
when I deleted the contents out of the Json file, then tried to run the program.
It's not currently set up for that. The program loaded nothing, tried to update
it with something. But there was nothing to update. 

"""