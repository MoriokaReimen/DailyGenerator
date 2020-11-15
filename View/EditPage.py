# -*- coding: utf-8 -*-
"""Tkinter Frame class for Edit page
"""
import tkinter as Tk
from tkinter import ttk
from tkinter import messagebox
import logging

class EditPage(Tk.Frame):
    """Tkinter Frame Class for Edit pgae

    Args:
        parent (Tk.Frame): parent Tkinter frame object
        control (Control): control object

    """
    def __init__(self, parent, control):
        # set variables
        self.parent = parent
        self.control = control
        self.task_id = -1
        self.man_hour = 0.0
        # Show Title
        Tk.Frame.__init__(self, self.parent.root)
        self.label = Tk.Label(self, text = "Edit Page")
        self.label.pack(side = Tk.TOP, anchor=Tk.NW)

        # Title entry
        self.lb_title = Tk.Label(self, text = "Title")
        self.lb_title.pack(side = Tk.TOP, anchor=Tk.NW)
        self.ed_title = Tk.Entry(self, width=50)
        self.ed_title.pack(side = Tk.TOP, anchor=Tk.NW)

        # Man-hour entry
        self.lb_man_hour = Tk.Label(self, text ="Man-hour")
        self.lb_man_hour.pack(side = Tk.TOP, anchor=Tk.NW)
        self.ed_man_hour = Tk.Label(self, text=self.man_hour)
        self.ed_man_hour.pack(side = Tk.TOP, anchor=Tk.NW)

        # increment Button
        self.bt_increment = Tk.Button(self, height=1, width=1)
        self.bt_increment["text"] = "+"
        self.bt_increment["command"] = lambda : self.increment_man_hour()
        self.bt_increment.pack(side = Tk.TOP, anchor=Tk.W)

        # decrement Button
        self.bt_decrement = Tk.Button(self, height=1, width=1)
        self.bt_decrement["text"] = "-"
        self.bt_decrement["command"] = lambda : self.decrement_man_hour()
        self.bt_decrement.pack(side = Tk.TOP, anchor=Tk.W)

        # Importance combobox
        self.lb_importance = Tk.Label(self, text = "Importance")
        self.lb_importance.pack(side = Tk.TOP, anchor=Tk.NW)
        self.cb_importance = ttk.Combobox(self)
        self.cb_importance['values'] = ('LOW', 'MIDDLE', 'HIGH')
        self.cb_importance.current(1)
        self.cb_importance.pack(side = Tk.TOP, anchor=Tk.NW)

        # Urgency combobox
        self.lb_urgency = Tk.Label(self, text = "Urgency")
        self.lb_urgency.pack(side = Tk.TOP, anchor=Tk.NW)
        self.cb_urgency = ttk.Combobox(self)
        self.cb_urgency['values'] = ('LOW', 'MIDDLE', 'HIGH')
        self.cb_urgency.current(1)
        self.cb_urgency.pack(side = Tk.TOP, anchor=Tk.NW)

        # detail entry
        self.lb_detail = Tk.Label(self, text = "Detail")
        self.lb_detail.pack(side = Tk.TOP, anchor=Tk.NW)
        self.ed_detail = Tk.Text(self, height=10)
        self.ed_detail.pack(side = Tk.TOP, anchor=Tk.NW)

        # memo entry
        self.lb_memo = Tk.Label(self, text = "Memo")
        self.lb_memo.pack(side = Tk.TOP, anchor=Tk.NW)
        self.ed_memo = Tk.Text(self, height=10)
        self.ed_memo.pack(side = Tk.TOP, anchor=Tk.NW)

        # Delete Button
        self.bt_delete = Tk.Button(self)
        self.bt_delete["text"] = "Delete"
        self.bt_delete["command"] = lambda : self.delete_task()
        self.bt_delete.pack(side = Tk.RIGHT)

        # Back Button
        self.bt_back = Tk.Button(self)
        self.bt_back["text"] = "Back"
        self.bt_back["command"] = lambda : self.parent.switch_frame("StartPage", 0)
        self.bt_back.pack(side = Tk.LEFT, anchor=Tk.E)

        # Create Button
        self.bt_back = Tk.Button(self)
        self.bt_back["text"] = "Update"
        self.bt_back["command"] = lambda : self.edit_task()
        self.bt_back.pack(side = Tk.LEFT)

    def increment_man_hour(self):
        """increment man hour
        """
        self.man_hour += 0.5
        self.ed_man_hour.config(text = self.man_hour)

    def decrement_man_hour(self):
        """decrement man hour

        """
        if self.man_hour >= 0.5:
            self.man_hour -= 0.5
            self.ed_man_hour.config(text = self.man_hour)

    def delete_task(self):
        """Delete task on database

        """
        title = self.ed_title.get().rstrip()
        if title:
            # Show popup
            MsgBox = Tk.messagebox.askquestion ('Delete {}?'.format(title),'Are you sure you want to delete the task',icon = 'warning')
            if MsgBox == 'yes':
                # Update task on database and return to Start page
                self.parent.switch_frame("StartPage", 0)
                self.control.delete_task(self.task_id)

    def edit_task(self):
        """Edit task on database

        """
        # fetch task data
        title = self.ed_title.get().rstrip()
        importance = {'LOW':0, 'MIDDLE':1, 'HIGH':2}[self.cb_importance.get()]
        urgency = {'LOW':0, 'MIDDLE':1, 'HIGH':2}[self.cb_urgency.get()]
        detail = self.ed_detail.get(1.0, Tk.END).rstrip()
        memo = self.ed_memo.get(1.0, Tk.END).rstrip()
        man_hour = self.man_hour
        if title :
            # Show popup
            MsgBox = Tk.messagebox.askquestion ('Update {}?'.format(title),'Are you sure you want to update the task',icon = 'warning')
            if MsgBox == 'yes':
                # Update task on database and return to Start page
                self.control.update_task(self.task_id, title, importance, urgency, detail, memo, man_hour)
                self.parent.switch_frame("StartPage", 0)

    def update(self, task_id):
        """Update handler which is called when Create page is displayed

        """
        logging.info("Page transition to Edit Page")
        # fetch task data from database
        task = self.control.get_task(task_id)[0]
        # clear task data
        self.ed_title.delete(0, Tk.END)
        self.cb_importance.current(1)
        self.cb_urgency.current(1)
        self.ed_detail.delete(1.0, Tk.END)
        self.ed_memo.delete(1.0, Tk.END)
        # Set task data
        self.task_id = task.task_id
        self.ed_title.insert(Tk.END, task.title.rstrip())
        self.cb_importance.current(task.importance)
        self.cb_urgency.current(task.urgency)
        self.ed_detail.insert(Tk.END, task.detail.rstrip())
        self.ed_memo.insert(Tk.END, task.memo.rstrip())
        self.man_hour = task.man_hour
        self.ed_man_hour.config(text = self.man_hour)
