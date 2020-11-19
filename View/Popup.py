# -*- coding: utf-8 -*-
"""Tkinter Frame class for Edit page
"""


def popupmsg(msg):
    popup = Tk.Tk()
    popup.wm_title(msg)
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()
