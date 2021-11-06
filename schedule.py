import calendar
import datetime
import time
import entry


class schedule:

    def __init__(self, user):
        self.calendar = calendar()
        self.dateTime = datetime.today()
        self.person = user
        
    def addEntry(self, new_entry):
        
        