from tkinter import *
from tkinter.ttk import *


def begin_button_press(xValue, yValue, seedValue):

    # placeholder!
    print(xValue, " ", yValue, " ", seedValue)


if __name__ == "__main__":
    screen = Tk()
    screen.grid_rowconfigure(0, minsize=30)
    screen.grid_rowconfigure(4, minsize=50)

    title = Label(screen, text="The Game of Life", font=44)
    title.grid(row=0, column=0, columnspan=2, pady=2)

    xLabel = Label(screen, text="Rows:")
    xLabel.grid(row=1, column=0, sticky=W, pady=2)

    yLabel = Label(screen, text="Columns:")
    yLabel.grid(row=2, column=0, sticky=W, pady=2)

    seedLabel = Label(screen, text="Seed:")
    seedLabel.grid(row=3, column=0, sticky=W, pady=2)

    xEntry = Entry(screen)
    yEntry = Entry(screen)
    seedEntry = Entry(screen)

    xEntry.grid(row=1, column=1, pady=2)
    yEntry.grid(row=2, column=1, pady=2)
    seedEntry.grid(row=3, column=1, pady=2)

    beginButton = Button(text="Start", width=25, command=lambda: begin_button_press(xEntry.get(), yEntry.get(), seedEntry.get()))
    beginButton.grid(row=4, column=0, columnspan=2, pady=2)

    mainloop()
