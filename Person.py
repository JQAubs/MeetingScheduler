import Group


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.schedule = Schedule()
        # group that I am apart of
        self.groups = set()
        # group that I got invited to
        self.invited_groups = set()

    def addEntry(self):
        return

    def createGroup(self):
        group = Group()
        self.groups.append(group)
        return

    def getGroupInvited(self):
        return self.invited_groups

    def acceptGroupInvite(self, group):
        for i in getGroupInvited():
            if i.group_id == group.group_id:
                self.groups.add(group)
                self.invited_groups.remove(group)
                return True
        return False