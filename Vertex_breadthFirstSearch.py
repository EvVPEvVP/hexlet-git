class Vertex:
    def __init__(self, val):
        self.Value = val
        self.hit = False

class SimpleGraph:
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        # Find the first empty slot in the vertex array
        index = 0
        while index < len(self.vertex) and self.vertex[index] is not None:
            index += 1
        if index == len(self.vertex):
            # Vertex array is full
            return False
        # Create a new Vertex object and add it to the array
        self.vertex[index] = Vertex(v)
        return True

    def RemoveVertex(self, v):
        # Remove all edges associated with vertex v
        for i in range(len(self.m_adjacency)):
            self.m_adjacency[v][i] = 0
            self.m_adjacency[i][v] = 0
        # Remove vertex v
        self.vertex[v] = None

    def IsEdge(self, v1, v2):
        return bool(self.m_adjacency[v1][v2])

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def BreadthFirstSearch(self, VFrom, VTo):
        # Mark all vertices as not visited
        for vertex in self.vertex:
            if vertex:
                vertex.hit = False

        # Initialize a queue to hold the vertices to visit
        queue = []
        # Mark the starting vertex as visited and enqueue it
        self.vertex[VFrom].hit = True
        queue.append(self.vertex[VFrom])
        # Initialize a dictionary to keep track of the parent vertex of each visited vertex
        parent = {self.vertex[VFrom]: None}

        # Loop until the queue is empty or the target vertex is found
        while queue:
            # Dequeue a vertex from the queue
            current_vertex = queue.pop(0)

            # If the current vertex is the target, reconstruct and return the shortest path
            if current_vertex == self.vertex[VTo]:
                path = []
                while current_vertex is not None:
                    path.insert(0, current_vertex)
                    current_vertex = parent[current_vertex]
                return path

            # Enqueue all unvisited adjacent vertices of the current vertex
            for i in range(len(self.vertex)):
                if self.m_adjacency[self.vertex.index(current_vertex)][i] and not self.vertex[i].hit:
                    self.vertex[i].hit = True
                    queue.append(self.vertex[i])
                    parent[self.vertex[i]] = current_vertex

        # No path found from the starting vertex to the target vertex
        return []



