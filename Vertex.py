class Vertex:
    def __init__(self, val):
        self.Value = val


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


