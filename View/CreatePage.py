
import tkinter as Tk
from tkinter import ttk


class CreatePage(Tk.Frame):
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
        # Show Title
        Tk.Frame.__init__(self, self.parent.root)
        self.label = Tk.Label(self, text = "Edit Page")
        self.label.pack(side = Tk.TOP, fill = Tk.X)

        # Title entry
        self.lb_title = Tk.Label(self, text = "Title")
        self.lb_title.pack()
        self.ed_title = Tk.Entry(self, width=50)
        self.ed_title.pack()

        # Importance combobox
        self.lb_importance = Tk.Label(self, text = "Importance")
        self.lb_importance.pack()
        self.cb_importance = ttk.Combobox(self)
        self.cb_importance['values'] = ('LOW', 'MIDDLE', 'HIGH')
        self.cb_importance.current(1)
        self.cb_importance.pack()

        # Urgency combobox
        self.lb_urgency = Tk.Label(self, text = "Urgency")
        self.lb_urgency.pack()
        self.cb_urgency = ttk.Combobox(self)
        self.cb_urgency['values'] = ('LOW', 'MIDDLE', 'HIGH')
        self.cb_urgency.current(1)
        self.cb_urgency.pack()

        # detail entry
        self.lb_detail = Tk.Label(self, text = "Detail")
        self.lb_detail.pack()
        self.ed_detail = Tk.Text(self, width=50, height=10)
        self.ed_detail.pack()

        # memo entry
        self.lb_memo = Tk.Label(self, text = "Memo")
        self.lb_memo.pack()
        self.ed_memo = Tk.Text(self, width=50, height=10)
        self.ed_memo.pack()

        # Back Button
        self.bt_back = Tk.Button(self)
        self.bt_back["text"] = "Back"
        self.bt_back["command"] = lambda : self.parent.switch_frame("StartPage", 0)
        self.bt_back.pack(side = "bottom")

        # Create Button
        self.bt_back = Tk.Button(self)
        self.bt_back["text"] = "Create"
        self.bt_back["command"] = lambda : self.create_task()
        self.bt_back.pack(side = "bottom")

    def create_task(self):
        title = self.ed_title.get()
        importance = {'LOW':0, 'MIDDLE':1, 'HIGH':2}[self.cb_importance.get()]
        urgency = {'LOW':0, 'MIDDLE':1, 'HIGH':2}[self.cb_urgency.get()]
        detail = self.ed_detail.get(1.0, Tk.END)
        memo = self.ed_memo.get(1.0, Tk.END)
        self.control.create_task(title, importance, urgency, detail, memo)
        msg = "Task {} Created".format(title)
        self.ed_title.delete(0, Tk.END)
        self.cb_importance.current(1)
        self.cb_urgency.current(1)
        self.ed_detail.delete(1.0, Tk.END)
        self.ed_memo.delete(1.0, Tk.END)
        CreatePage.popupmsg(msg)

    def update(self, event):
        print(event)
        print("update Create Page")
