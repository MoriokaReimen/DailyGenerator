import tkinter as Tk
from tkinter import ttk

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
        self.bt_back["command"] = lambda : self.parent.switch_frame("StartPage", 0)
        self.bt_back.pack(side = "bottom")

    def update(self, event):
        print("update Generate Page")
        print(event)
        self.daily.delete(1.0, Tk.END)
        self.daily.insert(Tk.END, self.control.get_daily())
        pass
