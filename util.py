from player import Player 
from room import Room
import random

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
    """
    Represent a graph as a dictionary of rooms 
    mapping exits to edges.
    """
    def __init__(self):
        self.last_id = None
        self.rooms = {}

    def add_room(self, room_id):
        """
        Add a room to the graph.
        """
        self.rooms[room_id] = set()

    def random_direction(self, direction):
        # Create empty array to hold explored exits
        explored_exits = []
        # Iterate through exits
        for i in player.current_room.get_exits():
            if i == '?':
                print("i EXITS: ", i)
                # Add explored exit to 
                explored_exits.add(i)

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