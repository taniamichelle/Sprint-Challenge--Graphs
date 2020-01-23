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

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        If both exist, add a connection from v1 to v2.
        If not, raise an error via Python exception.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create stack 
        stack = Stack()  
        # Put the starting point in it
        stack.push(starting_vertex)
        # Create set to mark explored exits
        explored = set()
        # While stack is not empty
        while stack.size() > 0:
            # remove item from top of stack
            curr_exit = stack.pop()
            # If not explored
            if curr_exit not in explored:
                # DO THE THING! (e.g. stop searching)
                print(curr_exit)
                # Add to explored
                explored.add(curr_exit)
                # Get neighbors for each exit
                for next_exit in self.get_neighbors(curr_exit):
                    # Add edge to stack
                    stack.push(next_exit)

    def dft_recursive(self, starting_vertex, explored=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if explored is None:
            explored = set()
        explored.add(starting_vertex)
        print(starting_vertex)
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in explored:
                self.dft_recursive(child_vert, explored)

    def dfs_recursive(self, starting_vertex, target_value, explored=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        
        if explored is None:
            # Initialize explored set
            explored = set()
        if path is None:
            # Initialize path as array b/c needs to be ordered
            path = []
        # Add starting_vertex to path
        explored.add(starting_vertex)
        # Add starting_vertex to path
        path = path + [starting_vertex]  
        # If at target, return path
        if starting_vertex == target_value:
            return path
        # Otherwise, call DFS_recursive on each neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in explored:
                new_path = self.dfs_recursive(neighbor, target_value, explored, path)
                if new_path:  # Catch if target does not exist
                    return new_path
        # for child_vert in self.vertices[starting_vertex]:
        #     if child_vert not in explored:
        #         new_path = self.dfs_recursive(child_vert, target_value, explored, path)
        #         if new_path:  # Catch if target does not exist
        #             return new_path
        return None  # Catch if target does not exist
    
    def bfs(self, starting_vertex, target_exit):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create empty queue
        queue = Queue()
        # enqueue a path to starting vertex id
        queue.enqueue([starting_vertex])
        # Create a set to store explored exits
        explored = set()
        # While q is not empty
        while queue.size() > 0:
            # Dequeue first path
            path = queue.dequeue()
            # Grab last exit from the path
            curr_exit = path[-1]
            # If that exit has not been explored
            if curr_exit not in explored:
                # Check if exit = '?'...
                # If it is, return the path
                if curr_exit == '?':
                    return path
                # Mark it as explored
                explored.add(curr_exit)
                # For each edge in item...
                # Add a path to its neighbors to the back of queue
                for next_exit in self.get_neighbors(curr_exit):
                    # Copy path
                    new_path = list(path)
                    # append neighbor to the back of queue
                    new_path.append(next_exit)
                    queue.enqueue(new_path)
        # Returns path as a list of room IDs
        return explored  
        # Convert explored to a list of n/s/e/w directions before 
        # you can add it to your traversal path.