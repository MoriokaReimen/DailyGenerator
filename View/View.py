# -*- coding: utf-8 -*-
"""View class which organize GUI part of app
"""

import tkinter as Tk
from tkinter import ttk

from Control import *
from .StartPage import *
from .CreatePage import *
from .EditPage import *
from .GeneratorPage import *

class View():
    """Tkinter Frame Generator for Edit pgae

    Args:
        control (Control): Control class object

    """
    def __init__(self, control):
        # Set up window
        self.root = Tk.Tk()
        self.root.title("Daily Generator Ver0.0")

        # pack all pages into list
        self.frames = {}
        for S,F in (("StartPage",StartPage), ("CreatePage",CreatePage), ("GeneratorPage",GeneratorPage), ("EditPage",EditPage)):
            frame = F(self, control)
            self.frames[S] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")

        # set Start page as initial page
        self.switch_frame("StartPage", 0)

    def start(self):
        """start app

        """
        self.root.mainloop()

    def switch_frame(self, page, task_id):
        """ switch displayed page

        Args:
            page (str): key string to select page
            task_id (Int): task id to show/edit

        """
        frame = self.frames[page]
        frame.tkraise()
        frame.update(task_id)
