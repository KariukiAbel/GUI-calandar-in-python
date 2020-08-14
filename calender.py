from tkinter import *
import calendar

# initializing tkinter
root = Tk()
root.title("My own GUI calendar")
year = 2020
myCal = calendar.calendar(year)
cal_year = Label(root, text=myCal, font="Consolas 10 bold")
cal_year.pack()

# running the program in ready state
root.mainloop()
