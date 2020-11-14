# -*- coding: utf-8 -*-
"""Control class which bridges View and Model
"""
import Model
import View

class Control():
    """Control class

    """
    def __init__(self):
        self.model = Model.Model(self)
        self.view = View.View(self)

    def start(self):
        """start app

        """
        self.view.start()

    def get_tasks(self):
        """get all task data from database

        """
        return self.model.db.fetch_all()

    def get_task(self, task_id):
        """delete task data from database
        Args:
            task_id (Int): task id

        """
        return self.model.db.fetch(task_id)

    def delete_task(self, task_id):
        """delete task data in database
        Args:
            task_id (Int): task id to be updated

        """
        self.model.db.delete_task(task_id)

    def create_task(self, title, importance, urgency, detail, memo):
        """create task data in database
        Args:
            title (str): title of task
            importance (Int): Importance of task
            urgency (Int): Urgency of task
            detail (str): detail of task
            memo (str): memo of task

        """
        task = Model.TableItem(0, True, title, importance, urgency, detail, memo)
        self.model.db.create(task)

    def update_task(self, task_id, title, importance, urgency, detail, memo):
        """updata task data in database
        Args:
            task_id (Int): task id to be updated
            title (str): title of task
            importance (Int): Importance of task
            urgency (Int): Urgency of task
            detail (str): detail of task
            memo (str): memo of task

        """
        task = Model.TableItem(task_id, True, title, importance, urgency, detail, memo)
        self.model.db.update(task)

    def get_daily(self):
        """Generate daily from database data
        """
        tasks = self.model.db.fetch_all()
        return self.model.daily_gen.generate(tasks)
