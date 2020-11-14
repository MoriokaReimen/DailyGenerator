from .Database import *
from .DailyGenerator import *

class Model():

    def __init__(self, control):
        self.db = Database("tasks.db")
        self.daily_gen = DailyGenerator()
        self.control = control

