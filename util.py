from player import Player 
from room import Room

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            # line 13 is O(n)
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """Represent a graph as a dictionary of rooms mapping labels to edges."""
    def __init__(self):
        self.last_id = None
        self.rooms = {}
        self.neighbors = {}

    def add_room(self, room_id):
        """
        Add a room to the graph.
        """
        self.rooms[self.last_id] = Room(name)
        self.neighbors[self.last_id] = set()

    def add_neighbor(self, room_id, neighbor_id):
        """
        Add bidirectional edge to the graph.
        If both exist, add a connection from room to neighbor.
        """
        if room_id == neighbor_id: 
            print("WARNING: Room cannot be its own neighbor.")
        elif neighbor_id in self.neighbors[room_id] or room_id in self.neighbors[neighbor_id]:
            print("WARNING: Neighbor already exists.")
        else:
            self.neighbors[room_id].add(neighbor_id)
            self.neighbors[neighbor_id].add(room_id)

    def get_neighbors(self, room_id):
        """
        Get all neighbors (edges) of a room.
        """
        return self.rooms[room_id]
    
    def traversal(self, rooms, starting_room):
        # Build traversal graph
        map_tree = Graph()
        for room in rooms:
            # Add rooms 
            map_tree.add_room(room[0])
            map_tree.add_room(room[1])
            # Add bidirectional neighbors
            map_tree.add_neighbor(room[0], room[1])
            map_tree.add_neighbor(room[1], room[0])

            # DFT
            # Create stack 
            stack = Stack()  
            # Put the starting room in stack
            stack.push(starting_room)
            # Create dictionary to mark explored rooms
            # key = player.current_room.id, 
            # value = {player.current_room.get_exits():player.travel(direction)} 
            visited_rooms = {} 
            # While stack is not empty
            while stack.size() > 0:
                # remove room from top of stack
                current_room = stack.pop()
                # If not visited_rooms
                if current_room not in visited_rooms:
                    # DO THE THING! (e.g. stop searching)
                    print(current_room)
                    # Add to visited_rooms
                    visited_rooms[current_room] = path
                    # Get neighbors 
                    for next_room in map_tree.get_neighbors(current_room):
                        # Add room to stack
                        stack.push(next_room)
            return map_tree.get_all_paths()
        
    def get_all_paths(self, room_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every room connected to that
        room with the shortest path between them.

        The key is the neighbor's ID and the value is the path.
        """
        traversal_path = []
        q = Queue()
        q.enqueue([room_id])

        # BFS
        while q.size() > 0:
            path = q.dequeue()
            neighbor = path[-1]
            print("get_all_paths PATH", path, "neighbor", neighbor)

            if neighbor not in traversal_path:
                traversal_path[neighbor] = path
                print("VISITED", visited)

            for neighbor in self.neighbors[neighbor]:
                path_copy = path.copy()
                path_copy.append(neighbor)
                print("PATH COPY", path_copy)
                q.enqueue(path_copy)

        return traversal_path

    # def dft(self, starting_room):
    # """
    # Print each room in depth-first order
    # beginning from starting_room.
    # """
    
    # # Create stack 
    # stack = Stack()  
    # # Put the starting room in stack
    # stack.push(starting_room)
    # # Create set to mark explored exits
    # visited_rooms = set()
    # # While stack is not empty
    # while stack.size() > 0:
    #     # remove room from top of stack
    #     current_room = stack.pop()
    #     # If not visited_rooms
    #     if curr_room not in visited_rooms:
    #         # DO THE THING! (e.g. stop searching)
    #         print(curr_room)
    #         # Add to visited_rooms
    #         visited_rooms.add(curr_room)
    #         # Get neighbors for each exit
    #         for next_exit in self.get_neighbors(curr_room):
    #             # Add edge to stack
    #             stack.push(next_exit)

    # def dft_recursive(self, starting_room, visited_rooms=None):
    #     """
    #     Print each vertex in depth-first order
    #     beginning from starting_room.

    #     This should be done using recursion.
    #     """
    #     if visited_rooms is None:
    #         visited_rooms = set()
    #     visited_rooms.add(starting_room)
    #     print(starting_room)
    #     for child_vert in self.vertices[starting_room]:
    #         if child_vert not in visited_rooms:
    #             self.dft_recursive(child_vert, visited_rooms)

    # def dfs_recursive(self, starting_room, target_value, visited_rooms=None, path=None):
        """
        Return a list containing a path from
        starting_room to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        
        if visited_rooms is None:
            # Initialize visited_rooms set
            visited_rooms = set()
        if path is None:
            # Initialize path as array b/c needs to be ordered
            path = []
        # Add starting_room to path
        visited_rooms.add(starting_room)
        # Add starting_room to path
        path = path + [starting_room]  
        # If at target, return path
        if starting_room == target_value:
            return path
        # Otherwise, call DFS_recursive on each neighbor
        for neighbor in self.get_neighbors(starting_room):
            if neighbor not in visited_rooms:
                new_path = self.dfs_recursive(neighbor, target_value, visited_rooms, path)
                if new_path:  # Catch if target does not exist
                    return new_path
        return None  # Catch if target does not exist
    
    # def bfs(self, starting_room, target_exit):
        """
        Return a list containing the shortest path from
        starting_room to last unexplored room you passed in
        breath-first order.
        """
        # Create empty queue
        queue = Queue()
        # enqueue a path to starting vertex id
        queue.enqueue([starting_room])
        # Create a set to store visited_rooms exits
        visited_rooms = set()
        # While q is not empty
        while queue.size() > 0:
            # Dequeue first path
            path = queue.dequeue()
            # Grab last exit from the path
            curr_room = path[-1]
            # If that exit has not been visited_rooms
            if curr_room not in visited_rooms:
                # Check if exit = '?'...
                # If it is, return the path
                if curr_room == '?':
                    return path
                # Mark it as visited_rooms
                visited_rooms.add(curr_room)
                # For each edge in item...
                # Add a path to its neighbors to the back of queue
                for next_exit in self.get_neighbors(curr_room):
                    # Copy path
                    new_path = list(path)
                    # append neighbor to the back of queue
                    new_path.append(next_exit)
                    queue.enqueue(new_path)
        # Returns path as a list of room IDs
        return visited_rooms  
        # Convert visited_rooms to a list of n/s/e/w directions before 
        # you can add it to your traversal path.