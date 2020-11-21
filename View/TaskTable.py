# -*- coding: utf-8 -*-
"""Tkinter widget class for displayin tasks
"""
import tkinter as tk
from .ScrollableFrame import *


class TaskTable(tk.Frame):
    def __init__(self, parent, view):
        tk.Frame.__init__(self, parent)
        self.view = view

        # add caption
        self.caption_frame = tk.Frame(self)
        self.caption_frame.pack(side=tk.TOP, anchor=tk.NW)

        # Title
        entry = tk.Label(
            self.caption_frame,
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
            self.caption_frame,
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
            self.caption_frame,
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
            self.caption_frame,
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
            self.caption_frame,
            text="Man-hour",
            width=10,
            justify=tk.LEFT,
            anchor=tk.W,
            relief=tk.RIDGE,
            fg="white",
            bg="black")
        entry.grid(row=0, column=4)

        # Show Entry
        self.task_table = VerticalScrolledFrame(self, height=700)
        self.task_table.pack(side=tk.TOP, anchor=tk.NW)

    def draw(self, tasks):
        self.flash()

        for j, task in enumerate(tasks):
            # Title
            entry = tk.Label(
                self.task_table.interior,
                text=task.title,
                width=25,
                justify=tk.LEFT,
                anchor=tk.W,
                relief=tk.RIDGE)
            entry.grid(row=j, column=0)

            # Importance
            importance = {
                0: "LOW", 1: "MIDDLE", 2: "HIGH"}[
                task.importance]
            entry = tk.Label(
                self.task_table.interior,
                text=importance,
                width=8,
                justify=tk.LEFT,
                anchor=tk.W,
                relief=tk.RIDGE)
            entry.grid(row=j, column=1)

            # Urgency
            urgency = {0: "LOW", 1: "MIDDLE", 2: "HIGH"}[task.urgency]
            entry = tk.Label(
                self.task_table.interior,
                text=urgency,
                width=8,
                justify=tk.LEFT,
                anchor=tk.W,
                relief=tk.RIDGE)
            entry.grid(row=j, column=2)

            # Create
            create_time = task.create_time[:16]
            entry = tk.Label(
                self.task_table.interior,
                text=create_time,
                width=15,
                justify=tk.LEFT,
                anchor=tk.W,
                relief=tk.RIDGE)
            entry.grid(row=j, column=3)

            # Man-hour
            man_hour = task.man_hour
            entry = tk.Label(
                self.task_table.interior,
                text=man_hour,
                width=10,
                justify=tk.LEFT,
                anchor=tk.W,
                relief=tk.RIDGE)
            entry.grid(row=j, column=4)

            # EditButton
            bt_edit = tk.Button(self.task_table.interior)
            bt_edit["text"] = "Edit"
            bt_edit["command"] = lambda task_id = task.task_id: self.view.switch_frame(
                "EditPage", task_id)
            bt_edit.grid(row=j, column=5)

    def flash(self):
        self.task_table.pack(side=tk.TOP, anchor=tk.NW, expand=True)
        # Clear table widgets
        for widget in self.task_table.interior.winfo_children():
            widget.destroy()

        # reset pack
        self.task_table.interior.pack_forget()
