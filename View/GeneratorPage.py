# -*- coding: utf-8 -*-
"""Tkinter Frame class for Generator page
"""
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

import logging


class GeneratorPage(tk.Frame):
    """Tkinter frame class for Edit pgae

    Args:
        parent (tk.Frame): parent Tkinter frame object
        control (Control): control object

    """

    def __init__(self, parent, control):
        # set variables
        self.parent = parent
        self.control = control
        tk.Frame.__init__(self, self.parent.root)

        # Show Title
        self.label = tk.Label(self, text="Generate Page")
        self.label.pack(side=tk.TOP, anchor=tk.NW)

        # Show Daily
        self.daily = tk.scrolledtext.ScrolledText(self)
        self.daily.insert(tk.END, control.get_daily())
        self.daily.pack(side=tk.TOP, anchor=tk.NW, expand=True)

        # Back Button
        self.bt_back = tk.Button(self)
        self.bt_back["text"] = "Back"
        self.bt_back["command"] = lambda: self.parent.switch_frame(
            "StartPage", 0)
        self.bt_back.pack(side=tk.LEFT)

    def update(self, task_id):
        """Update handler which is called when Generator page is displayed

        """
        logging.info("update Generate Page")
        # update daily
        self.daily.delete(1.0, tk.END)
        self.daily.insert(tk.END, self.control.get_daily())
