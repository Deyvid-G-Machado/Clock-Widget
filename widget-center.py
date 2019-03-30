from tkinter import *
from time import strftime

root = Tk()

def startclock():
    x = int(ed1.get())
    y = int(ed2.get())
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

lb1 = Label(root, text="Put the location that will be the widget:")
lb2 = Label(root, text="Distance from left: ")
lb3 = Label(root, text="Distance from top: ")

ed1 = Entry(root)
ed2 = Entry(root)

bt1 = Button(root,text="Confirmar", command=startclock)

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0, stick=W)
lb3.grid(row=2, column=0, stick=W)

ed1.grid(row=1, column=1, stick=W)
ed2.grid(row=2, column=1, stick=W)

bt1.grid(row=3, column=0, stick=W)

root.geometry('370x100+1+80')
root.mainloop()
