# import tkinter module
from tkinter import *
from tkinter.ttk import *

# creating main tkinter window/toplevel
master = Tk()

# this wil create a label widget
l0 = Label(master, text="The Game of Life")
l1 = Label(master, text="Rows:")
l2 = Label(master, text="Columns:")
l3 = Label(master, text="Seed:")
l4 = Button(text="Start", width=25)

l0.config(font=44)

# grid method to arrange labels in respective
# rows and columns as specified
l0.grid(row=0, column=0, columnspan=2, pady=2)
l1.grid(row=1, column=0, sticky=W, pady=2)
l2.grid(row=2, column=0, sticky=W, pady=2)
l3.grid(row=3, column=0, sticky=W, pady=2)
l4.grid(row=4, column=0, columnspan=2, pady=2)

master.grid_rowconfigure(0, minsize=30)
master.grid_rowconfigure(4, minsize=50)

# entry widgets, used to take entry from user
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

# this will arrange entry widgets
e1.grid(row=1, column=1, pady=2)
e2.grid(row=2, column=1, pady=2)
e3.grid(row=3, column=1, pady=2)

# infinite loop which can be terminated by keyboard
# or mouse interrupt
mainloop()
