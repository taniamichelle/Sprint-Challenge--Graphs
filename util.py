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

    