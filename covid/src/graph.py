class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.infected = []      # Not sure if we need other attributes than nodes and edges
        self.chance1 = 0
        self.change2 = 0

    # Maybe useful
    def find_cliques(self):
        print('hi')
