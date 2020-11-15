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

    """
    task_id: int
    active: bool
    title: str
    importance: int
    urgency: int
    detail: str
    memo: str
    create_time: datetime.datetime
