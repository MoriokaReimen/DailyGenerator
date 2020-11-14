import tkinter as Tk

class View():
    def __init__(self):
        # Set up window
        self.root = Tk.Tk()
        self.root.title("Daily Generator Ver0.0")
        self.root.geometry('300x200')
        self.frames = {}
        for F in (StartPage, EditPage, GeneratePage):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")
            self.switch_frame(StartPage)

    def start(self):
        self.root.mainloop()

    def switch_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

class StartPage(Tk.Frame):
    def __init__(self, parent):
        # Show Title
        Tk.Frame.__init__(self, parent.root)
        label = Tk.Label(self, text = "Table Task")
        label.pack(side = Tk.TOP, fill = Tk.X)

        # Edit Button
        self.bt_new_item = Tk.Button(self)
        self.bt_new_item["text"] = "Create New Item"
        self.bt_new_item["command"] = lambda : parent.switch_frame(EditPage)
        self.bt_new_item.pack(side = "bottom")

        # Generate Daily Button
        self.bt_generate = Tk.Button(self)
        self.bt_generate["text"] = "Generate Daily"
        self.bt_generate["command"] = lambda : parent.switch_frame(GeneratePage)
        self.bt_generate.pack(side = "bottom")

        # Show Entry
        frame2 = Tk.Frame(self)
        frame2.pack(side=Tk.TOP, fill=Tk.X)
        entry = Tk.Entry(frame2, width=10, fg='blue')
        entry.grid(row= 0, column=0)

class EditPage(Tk.Frame):
    def __init__(self, parent):
        # Show Title
        Tk.Frame.__init__(self, parent.root)
        label = Tk.Label(self, text = "Edit Page")
        label.pack(side = Tk.TOP, fill = Tk.X)

        # Back Button
        self.bt_back = Tk.Button(self)
        self.bt_back["text"] = "Back"
        self.bt_back["command"] = lambda : parent.switch_frame(StartPage)
        self.bt_back.pack(side = "bottom")

class GeneratePage(Tk.Frame):
    def __init__(self, parent):
        # Show Title
        Tk.Frame.__init__(self, parent.root)
        label = Tk.Label(self, text = "Generate Page")
        label.pack(side = Tk.TOP, fill = Tk.X)

        # Back Button
        self.bt_back = Tk.Button(self)
        self.bt_back["text"] = "Back"
        self.bt_back["command"] = lambda : parent.switch_frame(StartPage)
        self.bt_back.pack(side = "bottom")

if __name__ == '__main__':
    view = View()
    view.start()
