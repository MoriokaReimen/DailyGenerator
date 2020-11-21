# -*- coding: utf-8 -*-
"""Tkinter Frame class for Edit page
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
import logging


class EditPage(tk.Frame):
    """Tkinter Frame Class for Edit pgae

    Args:
        parent (tk.Frame): parent Tkinter frame object
        control (Control): control object

    """

    def __init__(self, parent, control):
        # set variables
        self.parent = parent
        self.control = control
        self.task_id = -1
        self.man_hour = 0.0
        # Show Title
        tk.Frame.__init__(self, self.parent.root)
        self.label = tk.Label(self, text="Edit Page")
        self.label.pack(side=tk.TOP, anchor=tk.NW)

        # Title entry
        self.lb_title = tk.Label(self, text="Title")
        self.lb_title.pack(side=tk.TOP, anchor=tk.NW)
        self.ed_title = tk.Entry(self, width=50)
        self.ed_title.pack(side=tk.TOP, anchor=tk.NW)

        # Man-hour entry
        self.lb_man_hour = tk.Label(self, text="Man-hour")
        self.lb_man_hour.pack(side=tk.TOP, anchor=tk.NW)

        self.spb_man_hour = tk.Spinbox(
            self, format="%.1f", from_=0.0, to=100.0, increment=0.5, state="readonly")
        self.spb_man_hour.pack(side=tk.TOP, anchor=tk.NW)

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
        self.ed_detail = tk.scrolledtext.ScrolledText(self, height=10)
        self.ed_detail.pack(side=tk.TOP, anchor=tk.NW, expand=True)

        # memo entry
        self.lb_memo = tk.Label(self, text="Memo")
        self.lb_memo.pack(side=tk.TOP, anchor=tk.NW)
        self.ed_memo = tk.scrolledtext.ScrolledText(self, height=10)
        self.ed_memo.pack(side=tk.TOP, anchor=tk.NW, expand=True)

        # Delete Button
        self.bt_delete = tk.Button(self)
        self.bt_delete["text"] = "Delete"
        self.bt_delete["command"] = lambda: self.delete_task()
        self.bt_delete.pack(side=tk.RIGHT)

        # Back Button
        self.bt_back = tk.Button(self)
        self.bt_back["text"] = "Back"
        self.bt_back["command"] = lambda: self.parent.switch_frame(
            "StartPage", 0)
        self.bt_back.pack(side=tk.LEFT, anchor=tk.E)

        # Create Button
        self.bt_back = tk.Button(self)
        self.bt_back["text"] = "Update"
        self.bt_back["command"] = lambda: self.edit_task()
        self.bt_back.pack(side=tk.LEFT)

    def delete_task(self):
        """Delete task on database

        """
        title = self.ed_title.get().rstrip()
        if title:
            # Show popup
            MsgBox = tk.messagebox.askquestion(
                'Delete {}?'.format(title),
                'Are you sure you want to delete the task',
                icon='warning')
            if MsgBox == 'yes':
                # Update task on database and return to Start page
                self.control.delete_task(self.task_id)
                self.parent.switch_frame("StartPage", 0)

    def edit_task(self):
        """Edit task on database

        """
        # fetch task data
        title = self.ed_title.get().rstrip()
        importance = {
            'LOW': 0, 'MIDDLE': 1, 'HIGH': 2}[
            self.cb_importance.get()]
        urgency = {'LOW': 0, 'MIDDLE': 1, 'HIGH': 2}[self.cb_urgency.get()]
        detail = self.ed_detail.get(1.0, tk.END).rstrip()
        memo = self.ed_memo.get(1.0, tk.END).rstrip()
        man_hour = self.spb_man_hour.get()
        if title:
            # Show popup
            MsgBox = tk.messagebox.askquestion(
                'Update {}?'.format(title),
                'Are you sure you want to update the task',
                icon='warning')
            if MsgBox == 'yes':
                # Update task on database and return to Start page
                self.control.update_task(
                    self.task_id,
                    title,
                    importance,
                    urgency,
                    detail,
                    memo,
                    man_hour)

    def update(self, task_id):
        """Update handler which is called when Create page is displayed

        """
        logging.info("Page transition to Edit Page")
        # fetch task data from database
        task = self.control.get_task(task_id)[0]
        # clear task data
        self.ed_title.delete(0, tk.END)
        self.spb_man_hour.configure(state='normal')
        self.spb_man_hour.delete(0, tk.END)
        self.cb_importance.current(1)
        self.cb_urgency.current(1)
        self.ed_detail.delete(1.0, tk.END)
        self.ed_memo.delete(1.0, tk.END)
        # Set task data
        self.task_id = task.task_id
        self.ed_title.insert(tk.END, task.title.rstrip())
        self.cb_importance.current(task.importance)
        self.cb_urgency.current(task.urgency)
        self.ed_detail.insert(tk.END, task.detail.rstrip())
        self.ed_memo.insert(tk.END, task.memo.rstrip())
        self.spb_man_hour.insert(0, task.man_hour)
        self.spb_man_hour.configure(state='readonly')
