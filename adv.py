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

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# DIRECTION PICKER
def random_direction(target_room):
    # Create empty list
    # direction = []
    # Iterate through exits
    # print("room in random_direction: ", target_room)
    exits = target_room.get_exits()
    # for i in exits:
    #     direction.append(i)
    # Shuffle list
    random.shuffle(exits)
    return exits[0]

# TRAVERSAL OVERVIEW:
def traversal(starting_room=None):
    room_id = player.current_room.id 
    # Create map_graph
    # map_graph = Graph(starting_room)
    # map_graph.add_room()
    # Create a stack to hold explored rooms
    stack = Stack()
    starting_room = player.current_room.id
    # Add starting_room to stack
    stack.push(starting_room)
    # Create empty dictionary to keep track of explored rooms...
    # {key: room_id, value: {exit: connecting_room_id}}
    explored_rooms = {}
    # Add starting_room
    # explored_rooms[starting_room] = {'n': '?', 's': '?', 'e': '?', 'w': '?'}
    # print("ROOM ID", room_id, "explored", explored_rooms)
    # While there are paths in stack...
    # print("Stack size1", stack.size())
    # room_id = player.current_room.id 
    # print("before while loop: Room_id: ", room_id, " Explored_rooms: ", explored_rooms)
    iterator = 0
    while stack.size() > 0:
        iterator += 1
        room_id = stack.pop()
        print("Iteration: ", iterator, ", Room_id: ", room_id, ", EXPLORED_rooms: ", explored_rooms)
        # If room not explored...
        if room_id not in explored_rooms:
            exits = player.current_room.get_exits()
            # Add current_room to explored_rooms
            explored_rooms[room_id] = dict()
            for i in exits:
                explored_rooms[room_id][i] = '?'
            # print("After adding '?' to exits: Room_id: ", room_id, ", Explored_rooms: ", explored_rooms)
            for chosen_direction in exits:
                chosen_neighbor = player.current_room.get_room_in_direction(chosen_direction)
                # print("chosen_direction: ", chosen_direction, ", chosen_neighbor: ", chosen_neighbor.id)
                if chosen_neighbor or explored_rooms[chosen_neighbor.id]:
                    stack.push(chosen_neighbor.id)
                    # print("stack: ", stack)
                    # Choose unexplored exit at random
                    # chosen_direction = random_direction(player.current_room)
                    # print("chosen_direction: ", chosen_direction)
                    # Get next room in chosen_direction
                    # chosen_direction = player.current_room.get_room_in_direction(chosen_direction)
                    # Update exits
                    explored_rooms[room_id][chosen_direction] = chosen_neighbor.id
                    # Travel through exit
                    player.travel(chosen_direction)
                    # Add direction to traversal_path
                    traversal_path.append(chosen_direction)
                    # print("CURRENT 4: ", player.current_room)
                    break
    return explored_rooms

print("TRAVERSAL: ", traversal())

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
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

