from graph import Graph


class Statistics:
    def __init__(self):
        self.graph = Graph()
        self.nr_initially_infected = 0
        self.infection_chance = 0
        self.lower_bound = 0
        self.upper_bound = 0
        self.positive = []             # list of positive nodes
        self.cluster_count = 0         # the number of clusters that have been found so far in the graph
        self.nr_tests = 0
        self.skip_test = False


