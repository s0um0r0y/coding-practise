class Graph:
    def __init__(self, size):
        self.size = size
        self.edges = []
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.edges.append((weight, u, v))

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def kruskals_algorithm(self):
        result = [] # minimum spanning tree
        i=0 # edge counter

        self.edges = sorted(self.edges, key=lambda item: item[2])

        parent, rank = [], []

        for node in range(self.size):
            parent.append(node)
            rank.append(0)

        while i < len(self.edges):
            u, v, weight = self.edges[i]
            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                result.append((u, v, weight))
                self.union(parent, rank, x, y)

        print("Edge \t Weight")
        for u,v,weight in result:
            print(f"{self.vertex_data[u]}-{self.vertex_data[v]} \t{weight}")