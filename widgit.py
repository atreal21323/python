from tkinter import *
from datetime import date


root = Tk()
root.title("getting started with widgets")
root.geometry("400x300")


lbl = Label(text= "hello!", fg="white", bg="#574186", height=1, width=300)

name_lbl = Label(text="enter your full name", bg="#932b2b")
name_entry = Entry()

def display():
    name = name_entry.get()

    global Message
    message = "welcome to the Application! \n"
    greet = "Hello "+name+"\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())



text_box = Text(height=3)

btn = Button(text="begin", command=display,  height=1, bg="#3f2626", fg="white")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()


root.mainloop()
