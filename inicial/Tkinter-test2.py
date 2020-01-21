import tkinter as tk

# --- functions ---
# `bind` sends `event` to function so it has to receive it
# `command=` doesn't sends `event` so it need some default value - ie. None
def on_button(event=None): 

    answer = entry.get().strip().lower()

    if answer in ("screen", "monitor"):
        # change text in existing label
        label['text'] = "Your {} is dirty. I can't see you.".format(answer)

    elif answer in ("mouse", "trackball"):
        label['text'] = "Your {} is too slow for me".format(answer)

    else:
        label['text'] = "{0}? What is {0}?".format(answer)

# --- main ---

root = tk.Tk()
root.geometry("300x300")
root.title("Try code")

entry = tk.Entry(root)
entry.pack()

# run function when in `entry` you press `ENTER` on keyboard 
entry.bind('<Return>', on_button) 

button = tk.Button(root, text="Enter", command=on_button)
button.pack()

label = tk.Label(root)
label.pack()

# activate `entry` so you don't have to click in `entry` to start typing
entry.focus() 

root.mainloop()