# -*- coding: utf-8 -*-
"""Model class which handles internal logic
"""
from .Database import *
from .DailyGenerator import *
from .SearchGenerator import *
import logging


class Model():
    """Model class

    """

    def __init__(self, control):
        logging.info("Model class created")
        self.db = Database("tasks.db")
        self.daily_gen = DailyGenerator()
        self.search_gen = SearchGenerator()
        self.control = control
