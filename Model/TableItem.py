# -*- coding: utf-8 -*-
"""Task data class
"""
from dataclasses import dataclass
from dataclasses import asdict
import datetime


@dataclass
class TableItem:
    """Task data class

    Args:
        task_id (int): task id
        active (bool): activation status
        title (str): task title
        importance (int): task importance LOW/MIDDLE/HIGH
        urgency (int): task urgency LOW/MIDDLE/HIGH
        detail (str): detail of task
        memo (str): memo of task
        man_hour (float): man hour of task
        create_time (datetime): task creation datetime

    """
    task_id: int
    active: bool
    title: str
    importance: int
    urgency: int
    detail: str
    memo: str
    man_hour: float
    create_time: datetime.datetime
