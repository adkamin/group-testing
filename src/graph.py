class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.cliques = []

    def __str__(self):
        graph_string = ""
        for node in self.nodes:
            graph_string += str(node) + "\n"
        graph_string += str(self.edges)
        return graph_string

    def create_nodes(self, list):
        for node in list:
            self.nodes.append(Node(node, self))

    def sort_by_degree(self):
        return sorted(self.nodes, key=lambda x: x.degree)

    def remove(self, index):
        # TODO do this
        pass

class Node:
    def __init__(self, i, graph):
        self.index = i
        self.neighbors = self.find_neighbors(graph.edges)
        self.degree = len(self.neighbors)

    def find_neighbors(self, edges):
        return [edge[(edge.index(self.index) + 1) % 2] for edge in edges if self.index in edge]

    def __str__(self):
        return f'{self.index}, {self.neighbors}, {self.degree}'

            


