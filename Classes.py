from queue import PriorityQueue
from itertools import combinations
#creating a class
class Graph:
    def __init__(self):
        self.users = {} 
        self.adjacency_list = {}
    #function that add user
    def addUser(self,user):
        ID,name,*interests = user
        if ID not in self.users:
            self.users[ID] = User(ID,name,interests)
        
    #function that add relathionship between 2 users 
    def addRelationship(self,ID1,ID2):
        if ID1 in self.users and ID2 in self.users:
            self.users[ID1].addFriend(ID2)
            self.users[ID2].addFriend(ID1)

    #function that remove user
    def removeUser(self,ID):
        if ID in self.users:
            self.users.pop(ID)
            
    #function that remove relationship            
    def removeRelationship(self,ID1,ID2):
        if ID1 in self.users and ID2 in self.users:
            self.users[ID1].removeFriend(ID2)
            self.users[ID2].removeFriend(ID1)

    #function that will list the friends
    def friends(self,ID):
        if ID in self.users:
            return self.users[ID].listOfFriends()
    
    #Breadth-First Search (BFS) 
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
    
    #Depth-First Search (DFS)
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
    #sorting users by their names
    def sortUsersByName(self):
        sorted_users = sorted(self.users.values(), key=lambda user: user.name)
        return sorted_users
    
    #sorting users by their friends number
    def sortUsersByNumFriends(self):
        sorted_users = sorted(self.users.values(), key=lambda user: len(user.friends), reverse=True)
        return sorted_users
    #using dijkstra's algorithm to find the shortest path between two users
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
        left_lst = users_list[left:left + left_size]
        right_lst = users_list[mid + 1:mid + 1 + right_size]

        index_l = 0
        index_r = 0
        index_merged = left
        while index_l < left_size and index_r < right_size:
            if key == 'name':
                if left_lst[index_l].name <= right_lst[index_r].name:
                    users_list[index_merged] = left_lst[index_l]
                    index_l += 1
                else:
                    users_list[index_merged] = right_lst[index_r]
                    index_r += 1
            elif key == 'friends':
                if len(left_lst[index_l].friends) >= len(right_lst[index_r].friends):
                    users_list[index_merged] = left_lst[index_l]
                    index_l += 1
                else:
                    users_list[index_merged] = right_lst[index_r]
                    index_r += 1

            index_merged += 1

        while index_l < left_size:
            users_list[index_merged] = left_lst[index_l]
            index_l += 1
            index_merged += 1 
        while index_r < right_size:
            users_list[index_merged] = right_lst[index_r]
            index_r += 1
            index_merged += 1

    #quick sort function
    def quicksort(self, users_list, left, right, key='name'):
        if left < right:
            pivot_index = self.partition(users_list, left, right, key)
            self.quicksort(users_list, left, pivot_index - 1, key)
            self.quicksort(users_list, pivot_index + 1, right, key)

    def partition(self, users_list, left, right, key):
        pivot = users_list[right]
        i = left - 1
        for j in range(left, right):
            if self.compare(users_list[j], pivot, key):
                i += 1
                users_list[i], users_list[j] = users_list[j], users_list[i]
        users_list[i + 1], users_list[right] = users_list[right], users_list[i + 1]
        return i + 1
    # Binary search function 
    def binarySearch(self, k, key='ID'):
        users_list = self.sortUsersByName() if key == 'name' else list(self.users.keys())
        low, high = 0, len(users_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if key == 'ID':
                if users_list[mid] == k:
                    return mid
                elif users_list[mid] < k:
                    low = mid + 1
                else:
                    high = mid - 1
            elif key == 'name':
                if users_list[mid].name == k:
                    return users_list[mid]
                elif users_list[mid].name < k:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


    def compare(self, user1, user2, key):
        if key == 'name':
            return user1.name <= user2.name
        elif key == 'friends':
            return len(user1.friends) >= len(user2.friends)
        return False
    

    def averageNumFriends(self):
        if not self.users:
            return 0.0  
        total_friends = sum(len(user.friends) for user in self.users.values())
        return total_friends / len(self.users)
    
    def networkDensity(self):
        num_users = len(self.users)
        if num_users < 2:
            return 0.0  
        max_possible_connections = num_users * (num_users - 1) / 2
        actual_connections = sum(len(friends) for friends in self.adjacency_list.values()) / 2
        return actual_connections / max_possible_connections
    
    def clusteringCoefficient(self):
        numOfTriangles = 0
        numOfTriplets = 0
        for user_id in self.adjacency_list:
            neighbors = list(self.adjacency_list[user_id])
            numOfNeighbors = len(neighbors)
            if numOfNeighbors < 2:
                continue  
            numOfTriplets += numOfNeighbors * (numOfNeighbors - 1) / 2
            for pair in combinations(neighbors, 2):
                if pair[1] in self.adjacency_list[pair[0]]:
                    numOfTriangles += 1  

        return numOfTriangles / numOfTriplets if numOfTriplets > 0 else 0
    #function that displays the statistics
    def displayStatistics(self):
        print("\nNetwork Statistics:")
        print(f"Average number of friends per user: {self.averageNumFriends():.2f}")
        print(f"Network density: {self.networkDensity():.2f}")
        print(f"Clustering coefficient: {self.clusteringCoefficient():.2f}")


    def suggestFriendsByMutualConnectionsAndInterests(self, user_id, num_suggestions=5):
        if user_id not in self.users:
            print(f"User with ID {user_id} does not exist.")
            return []
        user = self.users[user_id]
        user_friends = set(user.listOfFriends())
        user_interests = set(user.interests)
        friend_suggestions = {}
        for friend_id, friend in self.users.items():
            if friend_id != user_id and friend_id not in user_friends:
                friend_friends = set(friend.listOfFriends())
                mutual_connections = len(user_friends.intersection(friend_friends))
                common_interests = len(user_interests.intersection(set(friend.interests)))
                score = mutual_connections + common_interests

                if score > 0:
                    friend_suggestions[friend_id] = score
        sorted_suggestions = sorted(friend_suggestions.items(), key=lambda x: x[1], reverse=True)
        suggested_friends = [self.users[user][0] for user, score in sorted_suggestions][:num_suggestions]
        return suggested_friends
    

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
    #creating users
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
    #testing functions created above
    print("BFS from ID 456:", graph.bfs(456))
    print("DFS from ID 456:", graph.dfs(456))
    print("BFS from ID 789:", graph.bfs(789))
    print("DFS from ID 789:", graph.dfs(789))

    print("Dijkstra's shortest distances from ID 123:", graph.dijkstra(123))
    
    #displaying unsorted graph
    print("Unsorted users in the graph:")
    print(graph)

    #displaying sorted graph
    sorted_by_name = graph.sortUsersByName()
    print("\nUsers sorted by name:")
    for user in sorted_by_name:
        print(user)

    sorted_by_num_friends = graph.sortUsersByNumFriends()
    print("\nUsers sorted by number of friends:")
    for user in sorted_by_num_friends:
        print(user)
    #using binary search to search by Id
    searchForID = 123
    index = graph.binarySearch(searchForID, key='ID')
    if index != -1:
        print(f"\nUser with ID {searchForID} found:")
        print(graph.users[searchForID])
    else:
        print(f"\nUser with ID {searchForID} not found.")

    #using binary search to search by Name
    searchForName = "Leen"
    user = graph.binarySearch(searchForName, key='name')
    if user != -1:
        print(f"\nUser with name '{searchForName}' found:")
        print(user)
    else:
        print(f"\nUser with name '{searchForName}' not found.")
    #showing statistics
    graph.displayStatistics()
    user_id = 123
    print(f"Suggestions for user {user_id} based on mutual connections and common interests:")
    print(graph.suggestFriendsByMutualConnectionsAndInterests(user_id))
    
main()     