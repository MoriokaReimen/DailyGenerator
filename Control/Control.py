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

    def get_tasks(self, only_active=False):
        """get all task data from database

        """
        return self.model.db.fetch_all(only_active)

    def get_task(self, task_id):
        """delete task data from database
        Args:
            task_id (Int): task id

        """
        return self.model.db.fetch(task_id)

    def search_task(self, keyword):
        """delete task data from database
        Args:
            keyword (str): keyword to search

        """
        return self.model.db.search(keyword)

    def delete_task(self, task_id):
        """delete task data in database
        Args:
            task_id (Int): task id to be deleted

        """
        self.model.db.delete_task(task_id)

    def create_task(
            self,
            title,
            importance,
            urgency,
            detail,
            memo,
            create_time):
        """create task data in database
        Args:
            title (str): title of task
            importance (Int): Importance of task
            urgency (Int): Urgency of task
            detail (str): detail of task
            memo (str): memo of task
            man_hour (Float): man hour for the task
            create_time (datetime): date of creation

        """
        task = Model.TableItem(
            0,
            True,
            title,
            importance,
            urgency,
            detail,
            memo,
            0.0,
            create_time)
        self.model.db.create(task)

    def update_task(
            self,
            task_id,
            title,
            importance,
            urgency,
            detail,
            memo,
            man_hour):
        """updata task data in database
        Args:
            task_id (Int): task id to be updated
            title (str): title of task
            importance (Int): Importance of task
            urgency (Int): Urgency of task
            detail (str): detail of task
            memo (str): memo of task
            man_hour (Float): man hour for the task

        """
        task = Model.TableItem(
            task_id,
            True,
            title,
            importance,
            urgency,
            detail,
            memo,
            man_hour,
            0)
        self.model.db.update(task)

    def get_daily(self):
        """Generate daily from database data
        """
        tasks = self.model.db.fetch_all(only_active=True)
        return self.model.daily_gen.generate(tasks)
