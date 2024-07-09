from queue import PriorityQueue
class Graph:
    def __init__(self):
        self.users = {} 
        self.adjacency_list = {}

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
    
    def sortUsersByName(self):
        sorted_users = sorted(self.users.values(), key=lambda user: user.name)
        return sorted_users
    

    def sortUsersByNumFriends(self):
        sorted_users = sorted(self.users.values(), key=lambda user: len(user.friends), reverse=True)
        return sorted_users

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
    
    def mergeSort(self, users_list, left, right, key='name'):
        if left < right:
            mid = (left + right) // 2
            self.mergeSort(users_list, left, mid, key)
            self.mergeSort(users_list, mid + 1, right, key)
            self.merge(users_list, left, mid, right, key)

    def merge(self, users_list, left, mid, right, key):
        left_size = mid - left + 1
        right_size = right - mid
        left_lst = [0] * left_size
        right_lst = [0] * right_size

        for i in range(left_size):
            left_lst[i] = lst[left + i]
        for j in range(right_size):
            right_lst[j] = lst[mid + 1 + j]
        left_lst = users_list[left:left + left_size]
        right_lst = users_list[mid + 1:mid + 1 + right_size]

        index_l = 0
        index_r = 0
        index_merged = left
        while index_l < left_size and index_r < right_size:
                index_l += 1
            else:
                lst[index_merged] = right_lst[index_r]
                index_r += 1
            index_merged += 1

        while index_l < left_size:
            lst[index_merged] = left_lst[index_l]
            index_l += 1
            index_merged += 1

        while index_r < right_size:
            lst[index_merged] = right_lst[index_r]
            index_r += 1
            index_merged += 1

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

    print("Dijkstra's shortest distances from ID 123:", graph.dijkstra(123))
    print("Unsorted users in the graph:")
    print(graph)

    sorted_by_name = graph.sortUsersByName()
    print("\nUsers sorted by name:")
    for user in sorted_by_name:
        print(user)

    sorted_by_num_friends = graph.sortUsersByNumFriends()
    print("\nUsers sorted by number of friends:")
    for user in sorted_by_num_friends:
        print(user)

    
    
main()     