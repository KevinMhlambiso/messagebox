from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo(title="the message",message="you are an idiot")
    messagebox.showwarning(title="WARNING",message="you have a VIRUS!")
    messagebox.showerror(title="ERROR",message="somithing wrong")
    messagebox.askokcancel(title="premition",message="are you sure about this")

windows = Tk()

button = Button(windows,command=click,text='click me')
button.pack()

windows.mainloop()