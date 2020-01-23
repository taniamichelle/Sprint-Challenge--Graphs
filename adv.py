from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()

# Map Options:
# You may uncomment the smaller graphs for dev and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

# Functions to Traverse or Search
def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create stack 
        stack = Stack()  
        # Put the starting point in it
        stack.push(starting_vertex)
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in stack
        while stack.size() > 0:
            # Pop first item
            vertex = stack.pop()
            # If not visited
            if vertex not in visited:
                # DO THE THING! (e.g. stop searching)
                print(vertex)
                # Add to visited
                visited.add(vertex)
                # Get neighbors for each edge in item
                for next_vert in self.get_neighbors(vertex):
                    # Add edge to stack
                    stack.push(next_vert)

def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)
player = Player(world.starting_room)

def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create empty stack 
        stack = Stack()  # Stack imported above
        # Add starting point as first path in stack 
        stack.push([starting_vertex])
        # Create set to store visited vertices
        visited = set()
        # stack is not empty
        while stack.size() > 0:
            # Remove path at top of stack
            path = stack.pop()  
            # Grab last vertex from path
            vertex = path[-1]  
            # If vertex has not been visited...
            if vertex not in visited:
                # Check if it's the target...
                # If so, return path
                if vertex == destination_vertex:
                    return path  # Return path we've built so far
                # Mark it as visited
                visited.add(vertex)
                # Get neighbors for each edge in item
                # by adding a path to neighbors to top of stack
                for next_vert in self.get_neighbors(vertex):
                    # Copy path to avoid 'pass by reference' bug
                    new_path = list(path)  # Makes copy rather than reference
                    new_path.append(next_vert)  # Add new vertex to copy
                    stack.push(new_path) 

def dfs_recursive(self, starting_vertex, target_value, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        
        if visited is None:
            # Initialize visited set
            visited = set()
        if path is None:
            # Initialize path as array b/c needs to be ordered
            path = []
        # Add starting_vertex to path
        visited.add(starting_vertex)
        # Add starting_vertex to path
        path = path + [starting_vertex]  
        # If at target, return path
        if starting_vertex == target_value:
            return path
        # Otherwise, call DFS_recursive on each neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, target_value, visited, path)
                if new_path:  # Catch if target does not exist
                    return new_path
        return None

def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create queue
        queue = Queue()
        # Put the starting point in it
        queue.enqueue(starting_vertex)
        # Make a set to store vertices we've visited
        visited = set()
        # While q is not empty
        while queue.size() > 0:
            # dequeue first path
            vertex = queue.dequeue()
            # ALTERNATE for queue ONLY: check first
            # queue[0]  
            # If not visited
            if vertex not in visited:
                # Do the thing! (e.g. stop searching)
                print(vertex)
                # # ALTERNATE for queue ONLY: print(queue[0])
                # Add to visited
                visited.add(vertex)
                # ALTERNATE for queue ONLY: visited.add(queue[0])
                # For each edge in item
                # Add each item to back of queue
                for next_vert in self.get_neighbors(vertex):
                    ## ALTERNATE for queue ONLY: for next_vert in self.get_neighbors(queue[0])
                    # Add edge to q
                    queue.enqueue(next_vert)
                    # ALTERNATE for queue ONLY: queue.dequeue  # Get rid of it here
        
def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create empty queue
        queue = Queue()
        # enqueue a path to starting vertex id
        queue.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While q is not empty
        while queue.size() > 0:
            # Dequeue first path
            path = queue.dequeue()
            # Grab last vertex from the path
            vertex = path[-1]
            # If that vertex has not been visited
            if vertex not in visited:
                # Check if it's the target...
                # If it is, return the path
                if vertex == destination_vertex:
                    return path
                # Mark it as visited
                visited.add(vertex)
                # For each edge in item...
                # Add a path to its neighbors to the back of queue
                for next_vert in self.get_neighbors(vertex):
                    # Copy path
                    new_path = list(path)
                    # append neighbor to the back of queue
                    new_path.append(next_vert)
                    queue.enqueue(new_path)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# CODE TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
