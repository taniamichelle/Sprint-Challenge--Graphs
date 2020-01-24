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
    def __init__(self, starting_room):
        self.last_id = None
        self.rooms = {}
        self.current_room = starting_room

    def add_room(self, room_id):
        """
        Add a room to the graph.
        """
        self.rooms[room_id] = set()
    
    # DIRECTION PICKER
    def random_direction(self):
        # Create empty list
        direction = []
        # Iterate through exits
        exits = player.current_room.get_exits()
        for i in exits:
            direction.append(i)
        # Shuffle list
        random.shuffle(direction)
        return direction[0]

    # TRAVERSAL OVERVIEW:
    def traversal(self, starting_room):
        traversal_path = []
        print("Current exits: ", player.current_room.get_exits())
        # Create a stack to hold explored rooms
        stack = Stack()
        # Add starting_room to stack
        stack.push(starting_room)
        # Create empty dictionary to keep track of explored rooms...
        # {key: room_id, value: {exit: connecting_room}}
        explored_rooms = {}
        # While there are paths in stack...
        while stack.size() > 0:
            # Remove top item from stack
            current_room = stack.pop()
            # Check if visited
            # If room not explored...
            if current_room not in explored_rooms:
                print(current_room)
                # Mark room as explored
                room_id = player.current_room.id
                explored_rooms[room_id] = {'exit': ''}
                # Add current_room to map
                self.add_room(room.id)
                for connecting_room in player.current_room.get_exits(connecting_room):
                    stack.push(connecting_room)
                    # Choose unexplored exit at random
                    direction = player.current_room.random_direction()
                    print(direction)
                    # Travel through exit
                    player.travel(direction)
                    # Add direction to traversal_path
                    traversal_path.append(direction)
                    # Connect rooms
                    player.current_room.connect_rooms(direction, current_room)
        return explored_rooms

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