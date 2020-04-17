from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


# Load world
world = World()

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

# Map Options:
# You may uncomment the smaller graphs for dev and testing purposes.
# map_file = "maps/test_line.txt"
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


def explore_maze(player):

    # BFS helper function
    def bfs(graph, start_vertex, target_vertex):
        # create a queue
        q = Queue()
        # enqueue path to start_vertex
        q.enqueue([(start_vertex, None)])
        # create set to store visited vertices
        visited = set()
        
        # while q is not empty
        while q.size() > 0:
            # dequeue first path
            path = q.dequeue()
            # grab vertex from end of the path
            vertex = path[-1][0]
            
            # check if it's been visited
            if vertex not in visited:
                # mark it visited
                visited.add(vertex)
                
                # check if it's the target
                if vertex == target_vertex:
                    return path
                
                # enqueue path to its neighbors
                for direction, room in graph[vertex].items():
                    # make copy of path
                    path_copy = path.copy()
                    # append neighbor
                    path_copy.append((room, direction))
                    # enqueue path_copy
                    q.enqueue(path_copy)
    
    # empty set for visited and dict for graph
    visited = set()
    graph = dict()

    # create room pointers
    prev_room = None
    dir_arr_from = None

    # direction reversal
    dir_rev = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

    while True:
        # until you deadend
        while prev_room != player.current_room.id:
            # print('CURR_ROOM: ', player.current_room.id)
            visited.add(player.current_room.id)
            
            # get exits
            exits = player.current_room.get_exits()
            
            # if room has not been visited
            if player.current_room.id not in graph:
                # add to graph
                graph[player.current_room.id] = dict()
                # add exits to graph as '?'
                for each_exit in exits:
                    graph[player.current_room.id][each_exit] = '?'

            # reverse pointers
            if prev_room is not None:
                graph[player.current_room.id][dir_rev[dir_arr_from]] = prev_room.id
            if prev_room is not None:
                graph[prev_room.id][dir_arr_from] = player.current_room.id
            

            # DFT - in unexplored direction
            for direction, room in graph[player.current_room.id].items():
                possible_exits = []
                if room == '?':
                    possible_exits.append(direction)
            
            if len(possible_exits) > 0:
                dir_to_travel = possible_exits.pop()
                
                # move pointers
                prev_room = player.current_room
                dir_arr_from = dir_to_travel

                # add travel_dir to traversal_path
                traversal_path.append(dir_to_travel)

                # player travel
                player.travel(dir_to_travel)
            
            else:
                break
        
        # BFS - find path to nearest unexplored room
        path_to_unexpl = bfs(graph, player.current_room.id, '?')
        
        # end loop if all rooms have been explored
        if path_to_unexpl is None:
            break

        # remove start_room b/c it is current room to avoid duplicates
        path_to_unexpl.pop(0)
        
        # travel path
        for room, direction in path_to_unexpl:
            # print('CURR_ROOM 2: ', player.current_room.id)
            # move pointers
            prev_room = player.current_room
            dir_arr_from = direction
            
            # traverse 
            player.travel(direction)
            # add to traversal_path
            traversal_path.append(direction)

# Run function
explore_maze(player)        
    
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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
