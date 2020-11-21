# -*- coding: utf-8 -*-
"""Tkinter Frame class for Search page
"""
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from .TaskTable import *
import logging
import datetime


class SearchPage(tk.Frame):
    """Tkinter Frame Class for Create pgae

    Args:
        parent (tk.Frame): parent Tkinter frame object
        control (Control): control object

    """

    def __init__(self, parent, control):
        self.parent = parent
        self.control = control
        # Show Title
        tk.Frame.__init__(self, self.parent.root)
        self.label = tk.Label(self, text="Search Page")
        self.label.pack(side=tk.TOP, anchor=tk.NW)

        # keyword Frame
        self.keyword_frame = tk.Frame(self)
        self.keyword_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Keyword entry
        self.lb_keyword = tk.Label(self.keyword_frame, text="Keyword:")
        self.lb_keyword.pack(side=tk.LEFT, anchor=tk.NW)
        self.ed_keyword = tk.Entry(self.keyword_frame, width=50)
        self.ed_keyword.pack(side=tk.LEFT, anchor=tk.NW)

        # seach button
        self.bt_search = tk.Button(self.keyword_frame)
        self.bt_search["text"] = "Search"
        self.bt_search["command"] = lambda: self.on_search()
        self.bt_search.pack(side=tk.LEFT, anchor=tk.NW)

        # Show Search Result
        self.search_result = tk.scrolledtext.ScrolledText(self)
        self.search_result.pack(side=tk.TOP, fill=tk.BOTH,
                                anchor=tk.NW, expand=True)

        # Button Frame
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(
            side=tk.BOTTOM, fill=tk.BOTH, anchor=tk.NW, expand=True)

        # Back Button
        self.bt_back = tk.Button(self.button_frame)
        self.bt_back["text"] = "Back"
        self.bt_back["command"] = lambda: self.parent.switch_frame(
            "StartPage", 0)
        self.bt_back.pack(side=tk.LEFT)

    def update(self, task_id):
        """Update handler which is called when Create page is displayed

        """
        logging.info("Page transition to Search Page")

    def on_search(self):
        keyword = self.ed_keyword.get().rstrip()
        # update Search Result
        self.search_result.delete(1.0, tk.END)
        self.search_result.insert(
            tk.END, self.control.get_search_result(keyword))
