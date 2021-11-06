import Person


class Group:
    def __init__(self, name, owner: Person):
        self.group_name = name
        self.owner = owner
        # invited but not yet accepted
        self.invited_users = set()
        # all accepted users in the group
        self.members = set()

    def getMembers(self):
        return self.members
