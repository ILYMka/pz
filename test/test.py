from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Привет мир")
root.geometry('300x40')


def button_clicked():
    print("hello world!")


def close():
    root.destroy()
    root.quit()


button = ttk.Button(root, text="Press me", command=button_clicked)
button.pack(fill=BOTH)
root.protocol('WM_DELETE_WINDOW', close)
root.mainloop()
