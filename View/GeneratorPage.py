# -*- coding: utf-8 -*-
"""Tkinter Frame class for Generator page
"""
import tkinter as Tk
from tkinter import ttk

import logging

class GeneratorPage(Tk.Frame):
    """Tkinter frame class for Edit pgae

    Args:
        parent (Tk.Frame): parent Tkinter frame object
        control (Control): control object

    """
    def __init__(self, parent, control):
        # set variables
        self.parent = parent
        self.control = control
        Tk.Frame.__init__(self, self.parent.root)

        # Show Title
        self.label = Tk.Label(self, text = "Generate Page")
        self.label.pack(side = Tk.TOP, anchor=Tk.NW)

        # Show Daily
        self.daily = Tk.Text(self)
        self.daily.insert(Tk.END, control.get_daily())
        self.daily.pack(side = Tk.TOP, anchor=Tk.NW)

        # Back Button
        self.bt_back = Tk.Button(self)
        self.bt_back["text"] = "Back"
        self.bt_back["command"] = lambda : self.parent.switch_frame("StartPage", 0)
        self.bt_back.pack(side = Tk.LEFT)

    def update(self, task_id):
        """Update handler which is called when Generator page is displayed

        """
        logging.info("update Generate Page")
        # update daily
        self.daily.delete(1.0, Tk.END)
        self.daily.insert(Tk.END, self.control.get_daily())
