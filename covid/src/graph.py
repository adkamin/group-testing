class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def __str__(self):
        return f'{self.nodes}, {self.edges}'

    def find_neighbors(self, node):
        return [edge[(edge.index(node) + 1) % 2] for edge in self.edges if node in edge]
        

class Clique:
    def __init__(self):
        pass
