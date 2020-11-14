from graph import Graph


class Specifics:
    def __init__(self):
        self.graph = Graph()            # TODO comment each line
        self.nr_initially_infected = 0
        self.lower_bound = 0
        self.upper_bound = 0
        self.infected = []               # list of positive nodes
        self.nr_tests = 0
        self.skip_lefthalf = False
        self.stop = False
        self.nr_estimated_infected = 0
        self.connectivity_degree = 0.0
        self.infection_degree = 0.0

    def reset(self):  # TODO what are all the values that need to be reset and why?
        self.graph.nodes = []
        self.graph.edges = []
        self.graph.node_indices = []
        self.nr_tests = 0
        self.stop = False
