class Graph:
    def __init__(self):
        self.users={} 
    def addUser(self,user):
        if user.ID not in self.users:
            self.users[user.ID]=user  
    def addRelationship(self,ID1,ID2):
        if ID1 in self.users and ID2 in self.users:
            self.users[ID1].Add[ID2]
            self.users[ID2].Add[ID1] 
class User:
    def __init__(self,ID,Name,Friends):
        self.ID=ID
        self.Name=Name
        self.Friends=Friends
    def Add(self,Friend):
        self.Friends.add(Friend)
    def Remove(self,Friend):
        if Friend in self.Friends:
            self.Friends.remove(Friend)
    def ListOfFriends(self):
        return self.Friends
    def __str__(self):
        return "ID",self.ID,"Name",self.Name,"Friends",ListOfFriends(Friends)

