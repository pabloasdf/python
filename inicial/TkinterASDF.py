import tkinter

root = tkinter.Tk()
root.geometry("300x300")
root.title("Try code")

entry = tkinter.Entry(root)
entry.pack()
print(entry.get())
def on_button():
    if entry.get() == "Screen" or entry.get() == "screen": #corrected
        slabel = tkinter.Label(root, text="Screen was entered")
        slabel.pack()
    else:
        tlabel = tkinter.Label(root, text="")
        tlabel.pack()

button = tkinter.Button(root, text="Enter", command=on_button)
button.pack()

root.mainloop()