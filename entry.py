from datetime import datetime, timedelta

class Entry:
    # Common constructor
    def __init__(self, start_time: datetime, end_time: datetime, title: str, description: str):
        self.start_time     = start_time
        self.end_time       = end_time
        self.title          = title
        self.description    = description

    # Common methods
    def get_start_time(self) -> datetime:
        return self.start_time
    
    def get_end_time(self) -> datetime:
        return self.end_time
    
    def get_duration(self) -> timedelta:
        return self.end_time - self.start_time