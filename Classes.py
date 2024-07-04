class Graph:
    def __init__(self):
        self.users={} 
    def addUser(self,user):
        if user.ID not in self.users:
            self.users[user.ID]=user   
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

