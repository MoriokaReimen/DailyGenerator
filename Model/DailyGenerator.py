# -*- coding: utf-8 -*-
"""Daily generator clss
"""

import logging
from .TableItem import *

class DailyGenerator():
    """Daily generator clss
    """

    def __init__(self):
        pass

    def generate(self, rows):
        # Set header of daily
        text = "Dear Someone\n\n"

        # Generate sentence for tasks
        for row in rows:
            if row.active:
                text += \
                    "Title:{title}\n" \
                    "====================\n" \
                    "Importance:\t{importance}\n" \
                    "Urgency:\t{urgency}\n" \
                    "Detail:\n{detail}\n\n" \
                    .format(**asdict(row))

        # set footer of daily
        text += "Regards"
        return text


    def __del__(self):
        logging.info("Daily file closed successfully.")
