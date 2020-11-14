import logging
from .TableItem import *

class DailyGenerator():
    def __init__(self):
        pass

    def generate(self, rows):
        text = "Dear Someone\n\n"
        for row in rows:
            if row.active:
                text += \
                    "Title:{title}\n" \
                    "====================\n" \
                    "Importance:\t{importance}\n" \
                    "Urgency:\t{urgency}\n" \
                    "Detail:\n{detail}\n\n" \
                    .format(**asdict(row))

        text += "Regards"
        return text


    def __del__(self):
        logging.info("Daily file closed successfully.")
