from tkinter import *
from time import *


def write():
    for x in range(1, 100):
        lbred.configure(text=x)
        sleep(0.2)
    root.after(1000, write)


root = Tk()
lbred = Label(root, text="Red", fg="Red")
lbred.pack()
write()
root.mainloop()
