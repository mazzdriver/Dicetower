from modules import *

# ------------------
# dices     =====x
# sides     =====x
# #	[Throw it!]
# ------------------
# ...
# ------------------
# Rolled: n n n n 
# 
#   [Roll again]
# ------------------

root = tkinter.Tk()
root.title(text.throw_it)
inputting = tkinter.Frame()
showdown = tkinter.Frame()

dices = tkinter.IntVar()
sides = tkinter.IntVar()
dices.set(2)
sides.set(6)

dices_label = tkinter.Label(inputting, textvariable=text.dices)
sides_label = tkinter.Label(inputting, textvariable=text.sides)
dices_menu = tkinter.Spinbox(inputting, from_=1, to=20)
sides_menu = tkinter.Spinbox(inputting, from_=1, to=20)

dices = dices_menu.get()
sides = sides_menu.get()

inputting.pack()
dices_label.grid(row=0, column=0)
sides_label.grid(row=1, column=0)
dices_menu.grid(row=0, column=1)
sides_menu.grid(row=1, column=1)

root.mainloop()


def show():
    pass


if __name__ == "__main__":
    show()
