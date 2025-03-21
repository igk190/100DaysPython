from tkinter import * 

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label["text"] = new_text

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24)) # initialize Label class, save to var
# my_label.pack()
# my_label["text"] = "testie"
# my_label.config(text="A text")
# my_label.place(x=100,y=600)
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)

# Button
button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button2 = Button(text="Click me too!", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = Entry(width=25)
# input.pack()ß
input.grid(column=3, row=2)









window.mainloop()