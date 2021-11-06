import datetime
import time
import entry
import person


class schedule:

    def __init__(self, user):
        self.dateTime = datetime.date.today()
        self.person = user
        self.events = dict()

    def addEntry(self, new_entry):
        if new_entry.start_time in self.events:
            self.events[str(new_entry.start_time.year)+str(new_entry.start_time.month)+str(new_entry.start_time.day)].append(new_entry)
        else:
            self.events[str(new_entry.start_time.year)+str(new_entry.start_time.month)+str(new_entry.start_time.day)] = [new_entry]

    def getEvents(self):
        return self.events.copy()

#ent1 = entry.Entry(datetime.datetime.today(), datetime.datetime.now(), 'test', 'fuck it')
#s1 = schedule(None)
#dt = datetime.datetime.today()
#print(dt.day, dt.month)

#s1.addEntry(ent1)
#print(s1)
#print(s1.events)
