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

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# DIRECTION PICKER
def random_direction():
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
def traversal(starting_room=None):
    # Create a stack to hold explored rooms
    stack = Stack()
    starting_room = player.current_room.id
    # Add starting_room to stack
    stack.push(starting_room)
    # Create empty dictionary to keep track of explored rooms...
    # {key: room_id, value: {exit: connecting_room_id}}
    explored_rooms = {}
    # Add starting_room
    room_id = player.current_room.id 
    explored_rooms[starting_room] = {'n': '?', 's': '?', 'e': '?', 'w': '?'}
    print("ROOM ID", room_id, "explored", explored_rooms)
    # While there are paths in stack...
    # print("Stack size1", stack.size())
    while stack.size() > 0:
        print("Stack size", stack.size())
        # Remove top item from stack
        current_room = stack.pop()
        print("CURRENT", current_room, "explored", explored_rooms)
        # Check if visited
        # If room not explored...
        if current_room not in explored_rooms:
            print("CURR", current_room, "explored", explored_rooms)
            exits = player.current_room.get_exits()
            # Iterate through list of exits 
            for i in range(len(exits) + 1):
                # Add current_room to map (explored_rooms)
                explored_rooms[room_id] = {exits[i]: '?'}
            print("CURR1", current_room, "explored1", explored_rooms)
            for neighbor in exits:
                # print("Current exits: ", player.current_room.get_exits())
                stack.push(neighbor)
                # Choose unexplored exit at random
                chosen_direction = random_direction()
                # Get next room in chosen_direction
                neighbor = player.current_room.get_room_in_direction(chosen_direction)
                # Update exits
                explored_rooms[room_id] = {chosen_direction: neighbor}
                print('Chosen direction', chosen_direction)  
                # Travel through exit
                player.travel(chosen_direction)
                # Add direction to traversal_path
                traversal_path.append(chosen_direction)
                print('curr room', current_room)
                # Connect rooms
                # player.current_room.connect_rooms(chosen_direction, current_room)
    return explored_rooms

# def bfs(self, starting_room, target_exit):
    # """
    # Return a list containing the shortest path from
    # starting_room to last unexplored room you passed in
    # breath-first order.
    # """
    # # Create empty queue
    # queue = Queue()
    # # enqueue a path to starting vertex id
    # queue.enqueue([starting_room])
    # # Create a set to store visited_rooms exits
    # visited_rooms = set()
    # # While q is not empty
    # while queue.size() > 0:
    #     # Dequeue first path
    #     path = queue.dequeue()
    #     # Grab last exit from the path
    #     curr_room = path[-1]
    #     # If that exit has not been visited_rooms
    #     if curr_room not in visited_rooms:
    #         # Check if exit = '?'...
    #         # If it is, return the path
    #         if curr_room == '?':
    #             return path
    #         # Mark it as visited_rooms
    #         visited_rooms.add(curr_room)
    #         # For each edge in item...
    #         # Add a path to its neighbors to the back of queue
    #         for next_exit in self.get_neighbors(curr_room):
    #             # Copy path
    #             new_path = list(path)
    #             # append neighbor to the back of queue
    #             new_path.append(next_exit)
    #             queue.enqueue(new_path)
    # # Returns path as a list of room IDs
    # return visited_rooms  
    # # Convert visited_rooms to a list of n/s/e/w directions before 
    # # you can add it to your traversal path.

# print("ROOM Exits", player.current_room.get_exits())
# print("get dir", player.current_room.get_exits())
# print("get coords", player.current_room.get_coords())
# print("connect rooms", player.current_room.connect_rooms())

print("traversal", traversal())

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
