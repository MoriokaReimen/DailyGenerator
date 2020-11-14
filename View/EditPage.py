import tkinter as Tk
from tkinter import ttk

class EditPage(Tk.Frame):
    @staticmethod
    def popupmsg(msg):
        popup = Tk.Tk()
        popup.wm_title(msg)
        label = ttk.Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()

    def __init__(self, parent, control):
        self.parent = parent
        self.control = control
        self.id = -1
        # Show Title
        Tk.Frame.__init__(self, self.parent.root)
        self.label = Tk.Label(self, text = "Edit Page")
        self.label.pack(side = Tk.TOP, anchor=Tk.NW)

        # Title entry
        self.lb_title = Tk.Label(self, text = "Title")
        self.lb_title.pack(side = Tk.TOP, anchor=Tk.NW)
        self.ed_title = Tk.Entry(self, width=50)
        self.ed_title.pack(side = Tk.TOP, anchor=Tk.NW)

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


    def delete_task(self):
        title = self.ed_title.get().rstrip()
        if title:
            self.parent.switch_frame("StartPage", 0)
            self.control.delete_task(self.id)
            msg = "Task {} Deleted".format(title)
            EditPage.popupmsg(msg)

    def edit_task(self):
        title = self.ed_title.get().rstrip()
        importance = {'LOW':0, 'MIDDLE':1, 'HIGH':2}[self.cb_importance.get()]
        urgency = {'LOW':0, 'MIDDLE':1, 'HIGH':2}[self.cb_urgency.get()]
        detail = self.ed_detail.get(1.0, Tk.END).rstrip()
        memo = self.ed_memo.get(1.0, Tk.END).rstrip()
        if title :
            self.control.update_task(self.id, title, importance, urgency, detail, memo)
            msg = "Task {} Updated".format(title)
            EditPage.popupmsg(msg)

    def update(self, event):
        task = self.control.get_task(event)[0]
        print("update Create Page")
        print(event)
        # delete all
        self.ed_title.delete(0, Tk.END)
        self.cb_importance.current(1)
        self.cb_urgency.current(1)
        self.ed_detail.delete(1.0, Tk.END)
        self.ed_memo.delete(1.0, Tk.END)
        # Set title
        self.id = task.id
        self.ed_title.insert(Tk.END, task.title.rstrip())
        self.cb_importance.current(task.importance)
        self.cb_urgency.current(task.urgency)
        self.ed_detail.insert(Tk.END, task.detail.rstrip())
        self.ed_memo.insert(Tk.END, task.memo.rstrip())
