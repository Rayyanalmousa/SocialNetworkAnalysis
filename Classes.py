class Graph:
    def __init__(self):
        self.users = {} 


    def addUser(self,user):
        ID,name,*interests = user
        if ID not in self.users:
            self.users[ID] = User(ID,name,interests)
        

    def addRelationship(self,ID1,ID2):
        if ID1 in self.users and ID2 in self.users:
            self.users[ID1].addFriend(ID2)
            self.users[ID2].addFriend(ID1)


    def removeUser(self,ID):
        if ID in self.users:
            self.users.pop(ID)
            
                
    def removeRelationship(self,ID1,ID2):
        if ID1 in self.users and ID2 in self.users:
            self.users[ID1].removeFriend(ID2)
            self.users[ID2].removeFriend(ID1)


    def friends(self,ID):
        if ID in self.users:
            return self.users[ID].listOfFriends()
    def bfs(self,ID):
        visited =set()
        queue = [start]
        result = []
        while queue:
            node =queue.pop(0)
            if node not in visited:
                visited.add(node)
                result.append(node)
                for friend in self.users[node].listOfFriends():
                    if friend not in visited:
                        queue.append
        return result                
    def dfs(self)


    def __str__(self):
        return "\n".join(str(user) for user in self.users.values())

class User:
    def __init__(self,ID,name,interests=None):
        self.ID = ID
        self.name = name
        self.friends = set() 
        self.interests = interests if interests else []

    def addFriend(self,friend):
        self.friends.add(friend)
        

    def removeFriend(self,friend):
        if friend in self.friends:
            self.friends.remove(friend)


    def listOfFriends(self):
        return list(self.friends)
    
    def updateProfile(self,**interests):
        for key ,value in interests.items():
            setattr(self,key,value)


    def __str__(self):
        return "ID: {}, Name: {}, Friends: {},interests:{}".format(self.ID, self.name, self.friends,self.interests)
    

    
def main():
    user1 = (123,"Rayyan","animals,shopping") 
    user2 = (456,"Leen","books")
    user3 = (789,"David","cars")
    user4 = (124,"Leo","animals")
    graph = Graph()


#Add the users to the graph
    graph.addUser(user1)
    graph.addUser(user2)
    graph.addUser(user3)
    graph.addUser(user4)

    graph.removeUser(user3)

    graph.addRelationship(123,789)
    graph.addRelationship(124,456)

    graph.removeRelationship(123,789)

    print(graph)

main() 