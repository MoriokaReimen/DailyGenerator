import tkinter as Tk
from tkinter import ttk
import datetime

from .CreatePage import *
from .GeneratorPage import *
from .EditPage import *
from Control import *

class StartPage(Tk.Frame):
    def __init__(self, parent, control):
        self.parent = parent
        self.control = control

        # Show Title
        Tk.Frame.__init__(self, self.parent.root)
        self.label = Tk.Label(self, text = "Task Table")
        self.label.pack(side = Tk.TOP, anchor = Tk.NW)

        # Show Entry
        self.frame2 = Tk.Frame(self)
        self.frame2.pack(side = Tk.TOP, anchor = Tk.NW)

        # Edit Button
        self.bt_new_item = Tk.Button(self)
        self.bt_new_item["text"] = "Create New Item"
        self.bt_new_item["command"] = lambda : self.parent.switch_frame("CreatePage", 0)
        self.bt_new_item.pack(side = Tk.RIGHT, anchor = Tk.SE)

        # Generate Daily Button
        self.bt_generate = Tk.Button(self)
        self.bt_generate["text"] = "Generate Daily"
        self.bt_generate["command"] = lambda : self.parent.switch_frame("GeneratorPage", 0)
        self.bt_generate.pack(side = Tk.RIGHT, anchor = Tk.SE)

    def update(self, task_id):
        # Clear table widgets
        for widget in self.frame2.winfo_children():
            widget.destroy()

        # reset pack
        self.frame2.pack_forget()

        # Title
        entry = Tk.Label(self.frame2, text = "title", width = 25, justify=Tk.LEFT, anchor=Tk.W, relief = Tk.RIDGE, fg="white", bg="black")
        entry.grid(row= 0, column=0)

        # Importance
        entry = Tk.Label(self.frame2, text = "importance", width = 8, justify=Tk.LEFT, anchor=Tk.W, relief = Tk.RIDGE, fg="white", bg="black")
        entry.grid(row= 0, column=1)

        # Urgency
        entry = Tk.Label(self.frame2, text = "urgency", width = 8, justify=Tk.LEFT, anchor=Tk.W, relief = Tk.RIDGE, fg="white", bg="black")
        entry.grid(row= 0, column=2)

        # Create
        entry = Tk.Label(self.frame2, text = "create", width = 15, justify=Tk.LEFT, anchor=Tk.W, relief = Tk.RIDGE, fg="white", bg="black")
        entry.grid(row= 0, column=3)

        # Man-hour
        entry = Tk.Label(self.frame2, text = "Man-hour", width = 10, justify=Tk.LEFT, anchor=Tk.W, relief = Tk.RIDGE, fg="white", bg="black")
        entry.grid(row= 0, column=4)

        tasks = self.control.get_tasks()
        j = 1
        for task in tasks:
            if task.active :
                # Title
                entry = Tk.Label(self.frame2, text = task.title, width = 25, justify=Tk.LEFT, anchor=Tk.W, relief = Tk.RIDGE)
                entry.grid(row= j, column=0)

                # Importance
                importance = {0 : "LOW", 1 : "MIDDLE", 2: "HIGH"}[task.importance]
                entry = Tk.Label(self.frame2, text = importance, width = 8, justify=Tk.LEFT, anchor=Tk.W, relief = Tk.RIDGE)
                entry.grid(row= j, column=1)

                # Urgency
                urgency = {0 : "LOW", 1 : "MIDDLE", 2: "HIGH"}[task.urgency]
                entry = Tk.Label(self.frame2, text = urgency, width = 8, justify=Tk.LEFT, anchor=Tk.W, relief = Tk.RIDGE)
                entry.grid(row= j, column=2)

                # Create
                create_time = task.create_time[:16]
                entry = Tk.Label(self.frame2, text = create_time, width = 15, justify=Tk.LEFT, anchor=Tk.W, relief = Tk.RIDGE)
                entry.grid(row= j, column=3)

                # Man-hour
                man_hour = task.man_hour
                entry = Tk.Label(self.frame2, text = man_hour, width = 10, justify=Tk.LEFT, anchor=Tk.W, relief = Tk.RIDGE)
                entry.grid(row= j, column=4)

                # EditButton
                bt_edit = Tk.Button(self.frame2)
                bt_edit["text"] = "Edit"
                bt_edit["command"] = lambda task_id = task.task_id : self.parent.switch_frame("EditPage", task_id)
                bt_edit.grid(row=j, column=5)

                # move to next line
                j += 1

        self.frame2.pack(side=Tk.TOP, anchor=Tk.NW)
