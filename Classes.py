from queue import PriorityQueue
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
    
    
    def bfs(self,start):
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
                        queue.append(friend)
        return result                
    
    
    def dfs(self,start):
        visited = set()
        stack = []
        result = []
        stack.append(start)
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(str(self.users[node]))
                for ID in self.friends(node)[::-1]:
                    if ID not in visited:
                        stack.append(ID)
        return result 


    def dijkstra(self, start):
        previous = {v: None for v in self.users.keys()}
        visited = {v: False for v in self.users.keys()}
        distances = {v: float("inf") for v in self.users.keys()}
        distances[start] = 0
        queue = PriorityQueue()
        queue.put((0, start))
        while not queue.empty():
            removed_distance, removed = queue.get()
            visited[removed] = True
            for neighbor in self.adjacency_list[removed]:
                if visited[neighbor]:
                    continue
                new_distance = removed_distance + 1  
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = removed
                    queue.put((new_distance, neighbor))
        return distances
    

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
    print("BFS from ID 456:", graph.bfs(456))
    print("DFS from ID 456:", graph.dfs(456))
    print("BFS from ID 789:", graph.bfs(789))
    print("DFS from ID 789:", graph.dfs(789))
main()     