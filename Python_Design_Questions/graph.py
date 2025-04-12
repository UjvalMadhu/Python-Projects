from collections import defaultdict

# 1. Undirected, Unweighted Graph using Adjacency List

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        # Adds edge between vertices u and v
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if u not in self.adj_list[u]:
            self.adj_list[v].append(u)
    
    def add_vertex(self, vertex):
        # Adds a vertex to the graph
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    
    def get_neighbors(self, vertex):
        # Returns the list of neighbors for the vertex
        return self.adj_list.get(vertex,[])

    def __str__(self):
        output = ""
        for vertex, neighbors in self.adj_list.items():
            output += f"{vertex} -> {','.join(map(str, neighbors))}\n"
        return output
    


# Testing:

my_graph = Graph()

my_graph.add_vertex("Rochester")
my_graph.add_edge("Rochester", "Buffalo")
my_graph.add_edge("Rochester", "Syracuse")
my_graph.add_edge("Syracuse","NYC")

print(my_graph)