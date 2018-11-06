from tkinter import *

window = Tk()
window.title("Unit Converter")

def kg_to_all():
    print("Success!")
    val = float(e1_value.get())
    kg_to_grams = str(val * 1000) + " grams"
    kg_to_pounds = str(val * 2.20462) + " pounds"
    kg_to_ounces = str(val * 35.274) + " ounces"
    t1.insert(END, kg_to_grams)
    t2.insert(END, kg_to_pounds)
    t3.insert(END, kg_to_ounces)

l1 = Label(window, text="kg")
l1.grid(row=0, column=0)

b1 = Button(window, text="Convert", command=kg_to_all)
b1.grid(row=0, column=2)

e1_value=StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=2, width=30)
t1.grid(row=1, column=0)

t2 = Text(window, height=2, width=30)
t2.grid(row=1, column=1)

t3 = Text(window, height=2, width=30)
t3.grid(row=1, column=2)

window.mainloop()
