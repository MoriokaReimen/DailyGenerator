# -*- coding: utf-8 -*-
"""ScrollableFrame Widget Class
"""

from tkinter import *
from tkinter.ttk import *


class VerticalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling
    """

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        self.canvas = Canvas(self, bd=0, highlightthickness=0,
                             yscrollcommand=vscrollbar.set, height=self.winfo_reqheight())
        self.canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=self.canvas.yview)

        # reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = Frame(self.canvas)
        self.interior_id = self.canvas.create_window(0, 0, window=self.interior,
                                                     anchor=NW)
        self.canvas.config(width=600)
        self.canvas.itemconfigure(
            self.interior_id, width=600)
