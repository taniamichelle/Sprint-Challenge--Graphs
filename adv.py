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

print("ROOM Exits", player.current_room.get_exits())
print("get dir", player.current_room.get_exits())
print("get coords", player.current_room.get_coords())
print("connect rooms", player.current_room.connect_rooms())

# TRAVERSAL OVERVIEW:
    # Start in starting_room
    # player.current_room.get_exits()
    # Create a stack to hold explored rooms
    # stack = Stack()
    # Add starting_room to stack
    # stack.push(starting_room)
    # Create empty dictionary to keep track of explored rooms...
    # {key: room_id, value: {exit: connecting_room}}
    # explored_rooms = {}
        # While there are paths in stack...
        # while stack.size() > 0:
            # Remove top item from stack
            # current_room = stack.pop()
            # Connect rooms
            # connect_rooms(self, direction, connecting_room)
            # Check if visited
            # If room not explored...
            # if current_room not in explored_rooms:
                # print(current_room)
                # Mark room as explored
                # explored_rooms.add(current_room)
                # for connecting_room in player.current_room.get_exits(connecting_room)
                    # stack.push(connecting_room)
                    # Choose unexplored exit at random
                    # Travel through exit
                    # player.travel(self, direction)
                    # Add direction to traversal_path
                    # traversal_path.append('direction')

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
