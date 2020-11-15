DailyGenerator
========================================================================
DailyGenerator with Python3 Tkinter

# How to use
* Requirement: python3
* Execute `python3 __main__.py` on command line
 
# How to change daily format
Tweak ./Model/DailyGenerator.py.

```python:Model/DailyGenerator.py
    def generate(self, rows):
        # Set header of daily
        text = "Dear Someone\n\n"

        # Generate sentence for tasks
        for row in rows:
            if row.active:
                text += \
                    "Title:{title} - {man_hour}H\n" \
                    "====================\n" \
                    "Importance:\t{importance}\n" \
                    "Urgency:\t{urgency}\n" \
                    "Detail:\n{detail}\n\n" \
                    .format(**asdict(row))

        # set footer of daily
        text += "Regards"
        return text
```
