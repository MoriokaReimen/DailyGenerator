import tkinter as tk
from tkinter import ttk
import datetime

from .CreatePage import *
from .GeneratorPage import *
from .EditPage import *
from .TaskTable import *
from Control import *


class StartPage(tk.Frame):
    def __init__(self, parent, control):
        self.parent = parent
        self.control = control

        # Show Title
        tk.Frame.__init__(self, self.parent.root)
        self.label = tk.Label(self, text="Task Table")
        self.label.pack(side=tk.TOP, anchor=tk.NW)

        # Draw task table
        self.task_table = TaskTable(self, parent)
        self.task_table.pack(side=tk.TOP, anchor=tk.NW)

        # Button Frame
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
        tasks = self.control.get_tasks(only_active=True)
        self.task_table.draw(tasks)
