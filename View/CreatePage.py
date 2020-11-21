# -*- coding: utf-8 -*-
"""Tkinter Frame class for Create page
"""
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import logging
import datetime


class CreatePage(tk.Frame):
    """Tkinter Frame Class for Create pgae

    Args:
        parent (tk.Frame): parent Tkinter frame object
        control (Control): control object

    """

    def __init__(self, parent, control):
        self.parent = parent
        self.control = control
        # Show Title
        tk.Frame.__init__(self, self.parent.root)
        self.label = tk.Label(self, text="Edit Page")
        self.label.pack(side=tk.TOP, anchor=tk.NW)

        # Title entry
        self.lb_title = tk.Label(self, text="Title")
        self.lb_title.pack(side=tk.TOP, anchor=tk.NW)
        self.ed_title = tk.Entry(self, width=50)
        self.ed_title.pack(side=tk.TOP, anchor=tk.NW)

        # Importance combobox
        self.lb_importance = tk.Label(self, text="Importance")
        self.lb_importance.pack(side=tk.TOP, anchor=tk.NW)
        self.cb_importance = ttk.Combobox(self)
        self.cb_importance['values'] = ('LOW', 'MIDDLE', 'HIGH')
        self.cb_importance.current(1)
        self.cb_importance.pack(side=tk.TOP, anchor=tk.NW)

        # Urgency combobox
        self.lb_urgency = tk.Label(self, text="Urgency")
        self.lb_urgency.pack(side=tk.TOP, anchor=tk.NW)
        self.cb_urgency = ttk.Combobox(self)
        self.cb_urgency['values'] = ('LOW', 'MIDDLE', 'HIGH')
        self.cb_urgency.current(1)
        self.cb_urgency.pack(side=tk.TOP, anchor=tk.NW)

        # detail entry
        self.lb_detail = tk.Label(self, text="Detail")
        self.lb_detail.pack(side=tk.TOP, anchor=tk.NW)
        self.ed_detail = tk.Text(self, height=10)
        self.ed_detail.pack(side=tk.TOP, anchor=tk.NW)

        # memo entry
        self.lb_memo = tk.Label(self, text="Memo")
        self.lb_memo.pack(side=tk.TOP, anchor=tk.NW)
        self.ed_memo = tk.Text(self, height=10)
        self.ed_memo.pack(side=tk.TOP, anchor=tk.NW)

        # Button Frame
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Back Button
        self.bt_back = tk.Button(self.button_frame)
        self.bt_back["text"] = "Back"
        self.bt_back["command"] = lambda: self.parent.switch_frame(
            "StartPage", 0)
        self.bt_back.pack(side=tk.LEFT)

        # Create Button
        self.bt_back = tk.Button(self.button_frame)
        self.bt_back["text"] = "Create"
        self.bt_back["command"] = lambda: self.create_task()
        self.bt_back.pack(side=tk.RIGHT)

    def create_task(self):
        """Create task on database

        """
        # fetch task data
        title = self.ed_title.get().rstrip()
        importance = {
            'LOW': 0, 'MIDDLE': 1, 'HIGH': 2}[
            self.cb_importance.get()]
        urgency = {'LOW': 0, 'MIDDLE': 1, 'HIGH': 2}[self.cb_urgency.get()]
        detail = self.ed_detail.get(1.0, tk.END).rstrip()
        memo = self.ed_memo.get(1.0, tk.END).rstrip()
        if(title):
            # Show popup
            MsgBox = tk.messagebox.askquestion(
                'Update {}?'.format(title),
                'Are you sure you want to update the task',
                icon='warning')
            if MsgBox == 'yes':
                # Create task on database
                self.control.create_task(
                    title,
                    importance,
                    urgency,
                    detail,
                    memo,
                    datetime.datetime.now())
                # Clear displayed data back to Start page
                self.ed_title.delete(0, tk.END)
                self.cb_importance.current(1)
                self.cb_urgency.current(1)
                self.ed_detail.delete(1.0, tk.END)
                self.ed_memo.delete(1.0, tk.END)
                self.parent.switch_frame("StartPage", 0)

    def update(self, task_id):
        """Update handler which is called when Create page is displayed

        """
        logging.info("Page transition to Create Page")
