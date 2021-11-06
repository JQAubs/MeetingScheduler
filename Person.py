class Person:

    def __init__(self, name, uuid, email, age):
        self.name = name
        self.uuid = uuid
        self.email = email
        self.age = age
        self.schedule = Schedule()
    
    def addEntry(self, entry):
        if self.schedule.checkConflict(entry):
            return False
        self.schedule.addEntry(entry)
        return True
    def createGroup(self):
        return
    