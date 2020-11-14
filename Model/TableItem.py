from dataclasses import dataclass
from dataclasses import asdict

@dataclass
class TableItem:
    id: int
    active: bool
    title: str
    importance: int
    urgency: int
    detail: str
    memo: str
