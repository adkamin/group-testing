from graph import Graph

class Statistics:
    def __init__(self):
        self.graph = Graph()
        self.dynamic_graph = Graph()
        self.nr_initially_infected = 0
        self.infection_chance = 0
        self.lower_bound = 0
        self.upper_bound = 0
        self.positive = []             # list of positive nodes
        self.cluster_count = 0         # number indicating the number of clusters that have been found so far in the graph

    def __str__(self):
        return f'({self.graph} \n {self.nr_initially_infected}, {self.infection_chance}, {self.lower_bound}, {self.upper_bound})'

