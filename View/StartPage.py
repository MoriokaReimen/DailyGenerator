import tkinter as tk
from tkinter import ttk
import datetime

from .CreatePage import *
from .GeneratorPage import *
from .EditPage import *
from Control import *
from .ScrollableFrame import *


class StartPage(tk.Frame):
    def __init__(self, parent, control):
        self.parent = parent
        self.control = control

        # Show Title
        tk.Frame.__init__(self, self.parent.root)
        self.label = tk.Label(self, text="Task Table")
        self.label.pack(side=tk.TOP, anchor=tk.NW)

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
        self.frame2 = VerticalScrolledFrame(self)
        self.frame2.pack(side=tk.TOP, anchor=tk.NW)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Edit Button
        self.bt_new_item = tk.Button(self.button_frame)
        self.bt_new_item["text"] = "Create New Item"
        self.bt_new_item["command"] = lambda: self.parent.switch_frame(
            "CreatePage", 0)
        self.bt_new_item.pack(side=tk.LEFT)

        # Generate Daily Button
        self.bt_generate = tk.Button(self.button_frame)
        self.bt_generate["text"] = "Generate Daily"
        self.bt_generate["command"] = lambda: self.parent.switch_frame(
            "GeneratorPage", 0)
        self.bt_generate.pack(side=tk.RIGHT)

    def update(self, task_id):
        # Clear table widgets
        for widget in self.frame2.interior.winfo_children():
            widget.destroy()

        # reset pack
        self.frame2.interior.pack_forget()

        tasks = self.control.get_tasks()
        j = 1
        for task in tasks:
            if task.active:
                # Title
                entry = tk.Label(
                    self.frame2.interior,
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
                    self.frame2.interior,
                    text=importance,
                    width=8,
                    justify=tk.LEFT,
                    anchor=tk.W,
                    relief=tk.RIDGE)
                entry.grid(row=j, column=1)

                # Urgency
                urgency = {0: "LOW", 1: "MIDDLE", 2: "HIGH"}[task.urgency]
                entry = tk.Label(
                    self.frame2.interior,
                    text=urgency,
                    width=8,
                    justify=tk.LEFT,
                    anchor=tk.W,
                    relief=tk.RIDGE)
                entry.grid(row=j, column=2)

                # Create
                create_time = task.create_time[:16]
                entry = tk.Label(
                    self.frame2.interior,
                    text=create_time,
                    width=15,
                    justify=tk.LEFT,
                    anchor=tk.W,
                    relief=tk.RIDGE)
                entry.grid(row=j, column=3)

                # Man-hour
                man_hour = task.man_hour
                entry = tk.Label(
                    self.frame2.interior,
                    text=man_hour,
                    width=10,
                    justify=tk.LEFT,
                    anchor=tk.W,
                    relief=tk.RIDGE)
                entry.grid(row=j, column=4)

                # EditButton
                bt_edit = tk.Button(self.frame2.interior)
                bt_edit["text"] = "Edit"
                bt_edit["command"] = lambda task_id = task.task_id: self.parent.switch_frame(
                    "EditPage", task_id)
                bt_edit.grid(row=j, column=5)

                # move to next line
                j += 1

        self.frame2.pack(side=tk.TOP, anchor=tk.NW, expand=True)
