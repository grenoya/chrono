#!/usr/bin/env python
from Tkinter import Tk, Label, Frame, Button, StringVar
from Tkinter import TOP, BOTTOM, LEFT, RIGHT, X
from time import gmtime, strftime


class Chrono():
    def __init__(self, master):
        self.master = master
        self.t0 = 0.
        self.time = StringVar()
        self.time.set(strftime("%H:%M:%S", gmtime(self.t0)))
        self.flag = 0


        self.affichageChrono = Frame(self.master)
        self.affichageChrono.pack(side=TOP, fill=X)
        self.chrono = Label(self.affichageChrono, textvariable=self.time)
        self.chrono.pack(side=TOP)

        self.affichageBoutons = Frame(self.master)
        self.affichageBoutons.pack(side=BOTTOM, fill=X)
        self.boutonStart = Button(self.affichageBoutons, text="Start",
                command=self.action)
        self.boutonStart.pack(side=LEFT)
        self.boutonStop = Button(self.affichageBoutons, text="Stop",
                command=self.stop)
        self.boutonStop.pack(side=LEFT)
        self.boutonReset = Button(self.affichageBoutons, text="Reset",
                command=self.reset)
        self.boutonReset.pack(side=LEFT)
        self.boutonExit = Button(self.affichageBoutons, text="Exit",
                command=self.master.quit)
        self.boutonExit.pack(side=RIGHT)

    def action(self):
        self.flag = 1
        self.start()

    def start(self):
        self.time.set(strftime("%H:%M:%S", gmtime(self.t0)))
        if self.flag == 0:
            return
        self.t0 += 1.
        self.master.after(1000, self.start)

    def stop(self):
        self.flag = 0

    def reset(self):
        self.t0 = 0.
        self.time.set(strftime("%H:%M:%S", gmtime(self.t0)))


if __name__ == "__main__":
    root = Tk()
    chro = Chrono(root)
    root.mainloop()
