import tkinter as Tk
from tkinter import ttk

class View():
    def __init__(self, control):
        # Set up window
        self.root = Tk.Tk()
        self.root.title("Daily Generator Ver0.0")
        self.root.geometry('300x200')
        self.frames = {}
        for F in (StartPage, CreatePage, GeneratePage):
            frame = F(self, control)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")

        self.switch_frame(StartPage)

    def start(self):
        self.root.mainloop()

    def switch_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

class StartPage(Tk.Frame):
    def __init__(self, parent, control):
        self.parent = parent
        self.control = control

        # Show Title
        Tk.Frame.__init__(self, self.parent.root)
        self.label = Tk.Label(self, text = "Table Task")
        self.label.pack(side = Tk.TOP, fill = Tk.X)

        # Edit Button
        self.bt_new_item = Tk.Button(self)
        self.bt_new_item["text"] = "Create New Item"
        self.bt_new_item["command"] = lambda : self.parent.switch_frame(CreatePage)
        self.bt_new_item.pack(side = "bottom")

        # Generate Daily Button
        self.bt_generate = Tk.Button(self)
        self.bt_generate["text"] = "Generate Daily"
        self.bt_generate["command"] = lambda : self.parent.switch_frame(GeneratePage)
        self.bt_generate.pack(side = "bottom")

        # Show Entry
        tasks = self.control.get_tasks()
        frame2 = Tk.Frame(self)
        frame2.pack(side=Tk.TOP, fill=Tk.X)
        for i, task in enumerate(tasks):
            entry = Tk.Entry(frame2, width=10, fg='blue')
            entry["text"] = task.title
            entry.grid(row= i, column=0)

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
        self.bt_back["command"] = lambda : self.parent.switch_frame(StartPage)
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
        self.bt_back["command"] = lambda : self.parent.switch_frame(StartPage)
        self.bt_back.pack(side = "bottom")

if __name__ == '__main__':
    view = View()
    view.start()
