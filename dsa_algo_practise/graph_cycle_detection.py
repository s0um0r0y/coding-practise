class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
        self.parent = [i for i in range(size)] # union find array

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def find(self, i):
        if self.parent[i] == 1:
            return i
        return self.find(self.parent[i])
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        print (f"Union of {x} and {y}, roots are {xroot} and {yroot}")
        self.parent[xroot] = yroot
        print (f"Parent array after union: {self.parent}")

    
