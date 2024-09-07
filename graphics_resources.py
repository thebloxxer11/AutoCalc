#Library for Standard TkInter Widgets

from tkinter import *
from tkinter import ttk
import math
#Text
class StringText(Frame):
    def __init__(self, defaultText=""):
        self.text = defaultText
        self.object = Text()
        self.object.pack()
        self.object.insert(INSERT, self.text)
        self.object.config(state=DISABLED, width=len(self.text), height=1)
        pass

    def updateText(self, newText):
        oldText = self.text
        self.text = newText
        self.object.config(state=NORMAL, width=len(self.text))
        self.object.replace("0.0", str(len(oldText))+".0", self.text)
        self.object.config(state=DISABLED)
        pass
#Button
class TextButton(Frame):
    def __init__(self, defaultText, func):
        self.object = Button(text=defaultText, command = func)
        self.object.pack()
        pass

    def invokeFunc(self):
        return self.object.invoke()
    def flash(self):
        self.object.flash()
#Slider
class Slider(Frame):
    def __init__(self, min, max, default, length, isHorz=False):
        self.value = DoubleVar()
        self.setValue(default)
        self.object = Scale(from_=min, to=max, variable=self.value, length=length)
        if isHorz:
            self.object.config(orient=HORIZONTAL)
        else:
            self.object.config(orient=VERTICAL)
        self.object.pack()
        pass

    def getValue(self):
        return self.value.get()
    def setValue(self, value):
        self.value.set(value)
        pass
#Text Entry
class StringEntry(Frame):
    def __init__(self, defaultText="", isCleared=False):
        self.isCleared = isCleared
        self.object = Entry()
        self.object.pack()
        self.entryText = StringVar()
        self.entryText.set(defaultText)
        self.object["textvariable"] = self.entryText
        self.object.bind('<Key-Return>', self.updateText)
        pass

    def updateText(self, event):
        print(self.entryText.get())
        if self.isCleared == True:
            self.entryText.set("")
        pass
#Canvas
class Sketch(Frame):
    def __init__(self, w, h, bg=""):
        self.object = Canvas(width=w, height=h, bg=bg)
        self.object.pack()
        pass

    def line(self, x0, y0, x1, y1, width, fill):
        return self.object.create_line(x0, y0, x1, y1, width=width , fill=fill)

    def arc(self, x, y, fill, outline, x1=None, y1=None, extent=180, start=0):
        if x1==None:
            x1=2*x
        if y1==None:
            y1=2*y
        if extent>=360:
            raise Exception("Invalid Argument: extent cannot be greater than or equal to 360; Use ellipse()")
        return self.object.create_arc([x, y, x1, y1], fill=fill, outline=outline, extent=extent, start=start)

    def ellipse(self, x0, y0, x1, y1, width, fill, outline):
        return self.object.create_oval(x0, y0, x1, y1, width=width, fill=fill, outline=outline)

    def quad(self, x0, y0 , x1, y1, fill, outline, width):
        return self.object.create_polygon(x0, y0, x0, y1,x1,y1,x1,y0,fill=fill, width=width, outline=outline)

    def ensc_poly(self, centerX, centerY, sides, radius, offset, fill, outline, width):
        points = []
        shiftAngle = float(360/sides)
        currentAngle=offset+(shiftAngle/2)
        for i in range(sides):
            currentAngle = (currentAngle+shiftAngle)%360.0
            x = int(radius*math.cos(math.radians(currentAngle))+centerX)
            points.append(x)
            y = int(radius*math.sin(math.radians(currentAngle))+centerY)
            points.append(y)
        points.append(points[0])
        points.append(points[1])
        return self.object.create_polygon(points, outline=outline, fill=fill, width=width)
