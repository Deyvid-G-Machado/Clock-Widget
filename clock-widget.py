#Creator: Deyvid gm
#GitHub: https://github.com/Srflash
#Add a clock widget on your PC made just with python!
#Note: This version of the project is only running on windows, and has been tested with python 3.6

from tkinter import *
from time import strftime

window = Tk()


def tic():
    rel['text'] = strftime('%H:%M:%S')

def tac():
    tic()
    rel.after(1000, tac)


rel = Label(window)
#Change the value below to increase or decrease the size of the widget!
rel['font'] = 'Helvetica 50 bold'
rel["fg"] = "white"
rel["bg"] = "black"
rel.pack()
tac()

window.overrideredirect(True)
window.attributes("-transparentcolor", "black")
#Edit the location where the widget will be on your monitor!
#To do this, edit the window.geometry below.
#Example +distance from the left of the monitor +distance from the top of the monitor.
window.geometry("+10+10")
window.mainloop()