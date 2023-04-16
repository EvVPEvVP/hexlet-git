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

    def DepthFirstSearch(self, VFrom, VTo):
        # Mark all vertices as not visited
        for vertex in self.vertex:
            if vertex:
                vertex.hit = False

        # Define a recursive helper function to perform DFS
        def dfs_helper(vertex):
            # Mark the current vertex as visited
            vertex.hit = True

            # If the current vertex is the target, return it
            if vertex == self.vertex[VTo]:
                return [vertex]

            # Recursively search all unvisited adjacent vertices of the current vertex
            for i in range(len(self.vertex)):
                if self.m_adjacency[self.vertex.index(vertex)][i] and not self.vertex[i].hit:
                    result = dfs_helper(self.vertex[i])
                    if result:
                        result.insert(0, vertex)
                        return result

            # No path found from the current vertex
            return None

        # Call the helper function with the starting vertex
        return dfs_helper(self.vertex[VFrom]) or []
