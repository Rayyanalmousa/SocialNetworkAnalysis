class Graph:
    def __init__(self):
        self.users={} 
    def addUser(self,user):
        if user.ID not in self.users:
            self.users[user.ID]=user  
    def addRelationship(self,ID1,ID2):
        if ID1 in self.users and ID2 in self.users:
            self.users[ID1].Add(ID2)
            self.users[ID2].Add(ID1)
    def removeUser(self,ID):
        if ID in self.users:
            self.users.pop(ID)
            self.users[ID].Remove(ID)
    def removeRelationship(self,ID1,ID2):
        if ID1 in self.users and ID2 in self.users:
            self.users[ID1].Remove(ID2)
            self.users[ID2].Remove(ID1)
    def friends(self,ID):
        if ID in self.users:
            self.users[ID].ListOfFriends()        
class User:
    def __init__(self,ID,Name,**interests):
        self.ID=ID
        self.Name=Name
        self.Friends=set()   
    def Add(self,Friend):
        self.Friends.add(Friend)
    def Remove(self,Friend):
        if Friend in self.Friends:
            self.Friends.remove(Friend)
    def ListOfFriends(self):
        return self.Friends
    def __str__(self):
        return "ID",self.ID,"Name",self.Name,"Friends"
    def updateProfile(self,**interests):
        
def main():
    user1=(123,"Rayyan")
    user2=(456,"Leen")
    user3=(789,"David")
    graph=Graph()
#Add the users to the graph
    graph.addUser(user1)
    graph.addUser(user2)
    graph.addUser(user3)
    graph.removeUser(user3)
main()