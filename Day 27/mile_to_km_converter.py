from tkinter import * 
KM = 1.609344

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=100, height=50)
window.config(padx=20, pady=20)

def button_clicked():
    miles_num = float(miles_entry.get())
    converted_km["text"] = round(miles_num * KM, 2)

miles_entry = Entry(width=20)
miles_entry.grid(column=1, row=0)

miles = Label(text="Miles", font=("Arial", 20))
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to", font=("Arial", 20))
is_equal_to.grid(column=0, row=1)

converted_km = Label(text="0", font=("Arial", 20))
converted_km.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 20))
km.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked) # tying function as command
button.grid(column=1, row=2)







window.mainloop()