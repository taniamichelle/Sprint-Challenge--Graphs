from room import Room
from player import Player
from world import World
from util import Stack, Queue, Graph

import random
from ast import literal_eval

# Load world
world = World()

# Map Options:
# You may uncomment the smaller graphs for dev and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

print("Player travel N", player.travel('n'))

# TRAVERSAL OVERVIEW:
    # Start in starting_room
    # Get exits
    # Create a stack to hold paths
    # Add starting_room path to stack
    # Create empty dictionary to keep track of explored rooms
        # While there are paths in stack...
            # Choose unexplored exit at random
            # Travel through exit
            # Connect rooms
            # Get exits
            # Check if visited
            # Remove last path from top of stack
            # Get last room id
            # If room unexplored...
                # Check for exits...
                # If exit = '?',
                    # Return path
                    # Mark path as explored
                # Get neighboring rooms iteratively...
                    # Copy path 
                    # Append next room to copy
                    # Add new path to top of stack

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
        
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
print("trav path", traversal_path)

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
