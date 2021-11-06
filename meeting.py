from entry import Entry
from Person import Person
from datetime import datetime

class Meeting(Entry):
    def __init__(self, host: Person, start_time: datetime, end_time: datetime, title: str, description: str=""):
        super().__init__(start_time, end_time, title, description)
        self.host = host