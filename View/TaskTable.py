# -*- coding: utf-8 -*-
"""Tkinter widget class for displayin tasks
"""
import tkinter as tk


class TaskTable(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # create Frame for table title
        self.title_frame = tk.Frame(self)
        self.title_frame.pack(side=tk.TOP)

        # Title
        entry = tk.Label(
            self.title_frame,
            text="title",
            width=25,
            justify=tk.LEFT,
            anchor=tk.W,
            relief=tk.RIDGE,
            fg="white",
            bg="black")
        entry.grid(row=0, column=0)

        # Importance
        entry = tk.Label(
            self.title_frame,
            text="importance",
            width=8,
            justify=tk.LEFT,
            anchor=tk.W,
            relief=tk.RIDGE,
            fg="white",
            bg="black")
        entry.grid(row=0, column=1)

        # Urgency
        entry = tk.Label(
            self.title_frame,
            text="urgency",
            width=8,
            justify=tk.LEFT,
            anchor=tk.W,
            relief=tk.RIDGE,
            fg="white",
            bg="black")
        entry.grid(row=0, column=2)

        # Create
        entry = tk.Label(
            self.title_frame,
            text="create",
            width=15,
            justify=tk.LEFT,
            anchor=tk.W,
            relief=tk.RIDGE,
            fg="white",
            bg="black")
        entry.grid(row=0, column=3)

        # Man-hour
        entry = tk.Label(
            self.title_frame,
            text="Man-hour",
            width=10,
            justify=tk.LEFT,
            anchor=tk.W,
            relief=tk.RIDGE,
            fg="white",
            bg="black")
        entry.grid(row=0, column=4)
