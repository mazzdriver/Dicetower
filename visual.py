from modules import *
import main


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
root.geometry('400x100')
inputting = tkinter.Frame()
showdown = tkinter.Frame()


def change_to_showdown():
    digits = [str(i) for i in (main.throw(dices.get(), sides.get()))]
    roll = ' '.join(digits)
    rolled_label = tkinter.Label(showdown, text=(text.rolled + roll))
    rolled_label.grid(padx=150)
    inputting.grid_remove()
    action_button.grid_remove()
    showdown.grid()
    again_button.grid(sticky='S')


def change_to_inputting():
    showdown.grid_remove()
    inputting.grid()
    dices_label.grid(row=0, column=0)
    sides_label.grid(row=1, column=0)
    dices_menu.grid(row=0, column=1)
    sides_menu.grid(row=1, column=1)
    action_button.grid(row=2, columnspan=2)


dices = tkinter.IntVar()
sides = tkinter.IntVar()
dices.set(2)
sides.set(6)
dices_label = tkinter.Label(inputting, text=text.dices)
sides_label = tkinter.Label(inputting, text=text.sides)
dices_menu = tkinter.Spinbox(inputting, from_=1, to=20, textvariable=dices)
sides_menu = tkinter.Spinbox(inputting, from_=1, to=20, textvariable=sides)
action_button = tkinter.Button(inputting, text=text.throw_it, command=change_to_showdown)
again_button = tkinter.Button(showdown, text=text.roll_again, command=change_to_inputting)

change_to_inputting()
root.mainloop()


# def show():
#     pass
#
#
# if __name__ == "__main__":
#     show()
