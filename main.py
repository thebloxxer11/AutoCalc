# Main Interface

from tkinter import *
from tkinter import ttk
import math
from time import sleep
import os

#import extrapolated resources
import calc_resources as calc
import graphics_resources as graphics


class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.canv = graphics.Sketch(512, 512, bg="grey")
        self.canv.ensc_poly(256,256,5,50,90,"black","black", 2)
        pass
     
    def buttonAction(self):
        selection = "Value = " + str(self.slider.getValue())
        self.text.updateText(selection)
        pass



if __name__ == "__main__":
    root = Tk()
    app = App(root)
    app.master.title("DSP Calc")
    app.master.geometry("1920x1080")
    root.mainloop()

