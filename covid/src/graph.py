class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def __str__(self):
        return f'{self.nodes}, {self.edges}'

    def create_nodes(self, list):
        for node in list:
            self.nodes.append(Node(node, self))
            

class Node:
    def __init__(self, i, graph):
        self.index = i
        self.neighbors = self.find_neighbors(graph.edges, self.index)
        self.degree = len(self.neighbors)
        self.nr_cliques = 0
        self.infected = False
        self.init_infected = False

    def __str__(self):
        return f'{self.index}, {self.neighbors}, {self.degree}, {self.nr_cliques}, {self.infected}, {self.init_infected}'


    def find_neighbors(self, edges, node):
        return [edge[(edge.index(node) + 1) % 2] for edge in edges if node in edge]


class Clique:
    def __init__(self):
        pass

