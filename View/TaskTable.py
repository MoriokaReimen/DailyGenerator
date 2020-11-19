# -*- coding: utf-8 -*-
"""Tkinter widget class for displayin tasks
"""
import tkinter as Tk


class TaskTable(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)

        # create Frame for table title
        self.title_frame = Tk.Frame(self)
        self.title_frame.pack(side=Tk.TOP)

        # Title
        entry = Tk.Label(
            self.title_frame,
            text="title",
            width=25,
            justify=Tk.LEFT,
            anchor=Tk.W,
            relief=Tk.RIDGE,
            fg="white",
            bg="black")
        entry.grid(row=0, column=0)

        # Importance
        entry = Tk.Label(
            self.title_frame,
            text="importance",
            width=8,
            justify=Tk.LEFT,
            anchor=Tk.W,
            relief=Tk.RIDGE,
            fg="white",
            bg="black")
        entry.grid(row=0, column=1)

        # Urgency
        entry = Tk.Label(
            self.title_frame,
            text="urgency",
            width=8,
            justify=Tk.LEFT,
            anchor=Tk.W,
            relief=Tk.RIDGE,
            fg="white",
            bg="black")
        entry.grid(row=0, column=2)

        # Create
        entry = Tk.Label(
            self.title_frame,
            text="create",
            width=15,
            justify=Tk.LEFT,
            anchor=Tk.W,
            relief=Tk.RIDGE,
            fg="white",
            bg="black")
        entry.grid(row=0, column=3)

        # Man-hour
        entry = Tk.Label(
            self.title_frame,
            text="Man-hour",
            width=10,
            justify=Tk.LEFT,
            anchor=Tk.W,
            relief=Tk.RIDGE,
            fg="white",
            bg="black")
        entry.grid(row=0, column=4)
