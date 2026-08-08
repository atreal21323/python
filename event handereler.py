from tkinter import *



window = Tk()
window.title("event handeler")
window.geometry("100x100")



def handle_keypress(event):
    """print the character associated to the key pressed"""
    print(event.char)


window.bind("<Key>", handle_keypress)


def handle_click(event):
    print("\the button has been SuCsEsSfUlLy been clicked!!!!!!! horrayy")

button = Button(text="CLICK ME FOR  viru--- i mean a prize")
button.pack()

button.bind("<Button-1>", handle_click)


window.mainloop()