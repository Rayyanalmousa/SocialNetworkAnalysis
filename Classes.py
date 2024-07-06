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
            self.users[ID1].remove(ID2)
            self.users[ID2].remove(ID1)
    def friends(self,ID):
        if ID in self.users:
            self.users[ID].listOfFriends()        
class User:
    def __init__(self,ID,name,**interests):
        self.ID=ID
        self.name=name
        self.friends=set() 
        for key ,value in interests.items():
            setattr(self,key,value)  
    def addFriend(self,friend):
        self.friends.add(friend)
    def removeFriend(self,friend):
        if friend in self.friends:
            self.friends.remove(friend)
    def listOfFriends(self):
        return self.friends
    def __str__(self):
        return "ID",self.ID,"Name",self.name,"Friends"
    def updateProfile(self,**interests):
        for key ,value in interests.items():
            setattr(self,key,value)
def main():
    user1=(123,"Rayyan")
    user2=(456,"Leen")
    user3=(789,"David")
    user4=(124,"Leo")
    graph=Graph()
#Add the users to the graph
    graph.addUser(user1)
    graph.addUser(user2)
    graph.addUser(user3)
    graph.addUser(user4)
    graph.removeUser(user3)
    User.addFriend(123,789)
    User.addFriend(124,456)
    User.removeFriend(123,789)

main()