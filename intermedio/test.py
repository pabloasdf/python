from tkinter import *       

# def func for button callback


def takes_input():
    
    textBox.insert(INSERT, inputBox_val.get())

# object for windows
window = Tk()
window.title("Learning GUI")

inputBox_val = StringVar()

# create button on windows
myBtn = Button(window, text="Click Me", command = takes_input)         

myBtn.grid(row = 0, column = 0)


# input filed
inputBox = Entry(window, textvariable = inputBox_val)
inputBox.grid(row = 0, column = 1)


# textBox filed
textBox = Text(window, height = 1, width = 20)
textBox.grid(row = 0, column =2)

window.mainloop()          