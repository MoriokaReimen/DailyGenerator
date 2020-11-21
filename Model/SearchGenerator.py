# -*- coding: utf-8 -*-
"""Search Result
"""

import logging
from .TableItem import *


class SearchGenerator():
    """Daily generator clss
    """

    def __init__(self):
        pass

    def generate(self, rows):
        # Set header of daily
        text = ""

        # Generate sentence for tasks
        for row in rows:
            if row.active:
                text += \
                    "Title:{title} - {man_hour}H\n" \
                    "====================\n" \
                    "Create Time:\n{create_time}\n" \
                    "Importance:\t{importance}\n" \
                    "Urgency:\t{urgency}\n" \
                    "Detail:\n{detail}\n" \
                    "Memo:\n{memo}\n\n" \
                    .format(**asdict(row))
        return text

    def __del__(self):
        logging.info("Search Generator closed successfully.")
