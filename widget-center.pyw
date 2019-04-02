from tkinter import *
from time import strftime
import os

root = Tk()

def load1():
    arq1 = open('coord-x.txt', 'r')
    textx = arq1.read()
    arq2 = open('coord-y.txt', 'r')
    texty = arq2.read()
    ed1.insert(INSERT,textx)
    ed2.insert(INSERT,texty)
    arq1.close()
    arq2.close()

def startclock():
    x = (ed1.get())
    y = (ed2.get())
    with open('coord-x.txt', 'w', encoding='utf8') as outfile:
        outfile.write(x)
    with open('coord-y.txt', 'w', encoding='utf8') as outfile:
        outfile.write(y)
    window = Tk()
    def tic():
        rel['text'] = strftime('%H:%M:%S')
    def tac():
        tic()
        rel.after(1000, tac)
    rel = Label(window)
    rel['font'] = 'Helvetica 50 bold'
    rel["fg"] = "white"
    rel["bg"] = "black"
    rel.pack()
    tac()
    window.overrideredirect(True)
    window.attributes("-transparentcolor", "black")
    window.geometry('+{}+{}'.format(x, y))
    window.mainloop()

def closewidget():
    root.destroy()
    os.system('taskkill /im pythonw.exe')

lb1 = Label(root, text="Put the location that will be the widget:")
lb2 = Label(root, text="Distance from left: ")
lb3 = Label(root, text="Distance from top: ")

ed1 = Entry(root)
ed2 = Entry(root)

bt1 = Button(root,text="Confirm", command=startclock)
bt2 = Button(root,text="Close Widget", command=closewidget)

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0, stick=W)
lb3.grid(row=2, column=0, stick=W)

ed1.grid(row=1, column=1, stick=W)
ed2.grid(row=2, column=1, stick=W)

bt1.grid(row=3, column=0, stick=W)
bt2.grid(row=4, column=0, stick=W)

load1()

root.geometry('370x120+1+80')
root.mainloop()
