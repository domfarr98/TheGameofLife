from tkinter import *
from tkinter.ttk import *
import src.program


def begin_button_press(xValue, yValue, seedValue):

    # close the entry window
    screen.destroy()

    # initiate the game window with desired configuration
    src.program.main_program(xValue, yValue, seedValue)


# only run window code if ran as main
if __name__ == "__main__":

    # create the screen and configure all rows
    screen = Tk()
    screen.grid_rowconfigure(0, minsize=30)
    screen.grid_rowconfigure(4, minsize=50)

    # create the title and add to grid
    title = Label(screen, text="The Game of Life", font=44)
    title.grid(row=0, column=0, columnspan=2, pady=2)

    # create the xLabel and add to grid
    xLabel = Label(screen, text="Rows:")
    xLabel.grid(row=1, column=0, sticky=W, pady=2)

    # create the yLabel and add to grid
    yLabel = Label(screen, text="Columns:")
    yLabel.grid(row=2, column=0, sticky=W, pady=2)

    # create the Seed Label and add to grid
    seedLabel = Label(screen, text="Seed:")
    seedLabel.grid(row=3, column=0, sticky=W, pady=2)

    # create the entry boxes and add them to grid
    xEntry = Entry(screen)
    yEntry = Entry(screen)
    seedEntry = Entry(screen)
    xEntry.grid(row=1, column=1, pady=2)
    yEntry.grid(row=2, column=1, pady=2)
    seedEntry.grid(row=3, column=1, pady=2)

    # create the begin button, configure and add to grid
    beginButton = Button(text="Start", width=25, command=lambda: begin_button_press(xEntry.get(), yEntry.get(), seedEntry.get()))
    beginButton.grid(row=4, column=0, columnspan=2, pady=2)

    # make sure program loops until further interaction
    mainloop()
