from tkinter import * 

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def button_clicked():
    new_text = input.get()
    miles["text"] = new_text

# miles1 = Label(text="Miles", font=("Arial", 20))
# miles1.grid(column=0, row=0)

x = Entry(width=20)
x.grid(column=1, row=0)

miles = Label(text="Miles", font=("Arial", 20))
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to", font=("Arial", 20))
is_equal_to.grid(column=0, row=1)

km = Label(text="Km", font=("Arial", 20))
km.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)







window.mainloop()