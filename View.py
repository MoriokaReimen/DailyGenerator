import tkinter as Tk
from tkinter import ttk

class View():
    def __init__(self, control):
        # Set up window
        self.root = Tk.Tk()
        self.root.title("Daily Generator Ver0.0")
        self.frames = {}
        for F in (StartPage, CreatePage, GeneratePage, EditPage):
            frame = F(self, control)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")

        self.switch_frame(StartPage, 0)

    def start(self):
        self.root.mainloop()

    def switch_frame(self, page, event):
        frame = self.frames[page]
        frame.tkraise()
        frame.update(event)

class StartPage(Tk.Frame):
    def __init__(self, parent, control):
        self.parent = parent
        self.control = control

        # Show Title
        Tk.Frame.__init__(self, self.parent.root)
        self.label = Tk.Label(self, text = "Table Task")
        self.label.pack(side = Tk.TOP, fill = Tk.X)

        # Show Entry
        self.frame2 = Tk.Frame(self)
        self.frame2.pack(side=Tk.TOP, fill=Tk.X)

        # Edit Button
        self.bt_new_item = Tk.Button(self)
        self.bt_new_item["text"] = "Create New Item"
        self.bt_new_item["command"] = lambda : self.parent.switch_frame(CreatePage, 0)
        self.bt_new_item.pack(side = "bottom")

        # Generate Daily Button
        self.bt_generate = Tk.Button(self)
        self.bt_generate["text"] = "Generate Daily"
        self.bt_generate["command"] = lambda : self.parent.switch_frame(GeneratePage, 0)
        self.bt_generate.pack(side = "bottom")

    def update(self, event):
        print(event)
        for widget in self.frame2.winfo_children():
            widget.destroy()

        self.frame2.pack_forget()
        tasks = self.control.get_tasks()
        j = 0
        for task in tasks:
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

            # EditButton
            bt_edit = Tk.Button(self.frame2)
            bt_edit["text"] = "Edit"
            bt_edit["command"] = lambda id = task.id : self.parent.switch_frame(EditPage, id)
            bt_edit.grid(row=j, column=3)

            # move to next line
            j += 1

        self.frame2.pack(side=Tk.TOP, fill=Tk.X)

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
        self.bt_back["command"] = lambda : self.parent.switch_frame(StartPage, 0)
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
        self.bt_back["command"] = lambda : self.parent.switch_frame(StartPage, 0)
        self.bt_back.pack(side = "bottom")

        # Create Button
        self.bt_back = Tk.Button(self)
        self.bt_back["text"] = "Update"
        self.bt_back["command"] = lambda : self.edit_task()
        self.bt_back.pack(side = "bottom")

        self.id = -1

    def edit_task(self):
        title = self.ed_title.get()
        importance = {'LOW':0, 'MIDDLE':1, 'HIGH':2}[self.cb_importance.get()]
        urgency = {'LOW':0, 'MIDDLE':1, 'HIGH':2}[self.cb_urgency.get()]
        detail = self.ed_detail.get(1.0, Tk.END)
        memo = self.ed_memo.get(1.0, Tk.END)
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
        self.ed_title.insert(Tk.END, task.title)
        self.cb_importance.current(task.importance)
        self.cb_urgency.current(task.urgency)
        self.ed_detail.insert(Tk.END, task.detail)
        self.ed_memo.insert(Tk.END, task.memo)

class GeneratePage(Tk.Frame):
    def __init__(self, parent, control):
        self.parent = parent
        self.control = control
        Tk.Frame.__init__(self, self.parent.root)

        # Show Title
        self.label = Tk.Label(self, text = "Generate Page")
        self.label.pack(side = Tk.TOP, fill = Tk.X)

        # Show Daily
        self.daily = Tk.Text(self)
        self.daily.insert(Tk.END, control.get_daily())
        self.daily.pack()

        # Back Button
        self.bt_back = Tk.Button(self)
        self.bt_back["text"] = "Back"
        self.bt_back["command"] = lambda : self.parent.switch_frame(StartPage, 0)
        self.bt_back.pack(side = "bottom")

    def update(self, event):
        print("update Generate Page")
        print(event)
        self.daily.delete(1.0, Tk.END)
        self.daily.insert(Tk.END, self.control.get_daily())
        pass

if __name__ == '__main__':
    view = View()
    view.start()
