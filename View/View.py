import tkinter as Tk
from tkinter import ttk
from .StartPage import *
from .CreatePage import *
from .EditPage import *
from .GeneratorPage import *
from Control import *

class View():
    def __init__(self, control):
        # Set up window
        self.root = Tk.Tk()
        self.root.title("Daily Generator Ver0.0")
        self.frames = {}
        for S,F in (("StartPage",StartPage), ("CreatePage",CreatePage), ("GeneratePage",GeneratePage), ("EditPage",EditPage)):
            frame = F(self, control)
            self.frames[S] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")

        self.switch_frame("StartPage", 0)

    def start(self):
        self.root.mainloop()

    def switch_frame(self, page, event):
        frame = self.frames[page]
        frame.tkraise()
        frame.update(event)
