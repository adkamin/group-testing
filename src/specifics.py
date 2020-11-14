from graph import Graph


class Specifics:
    def __init__(self):
        self.graph = Graph()             # graph object
        self.nr_initially_infected = 0   # number of initially infected people
        self.lower_bound = 0             # upper bound
        self.upper_bound = 0             # lower bound
        self.infected = []               # list of nodes which were found to be positive
        self.nr_queries = 0              # number of queries to the server
        self.skip_lefthalf = False       # boolean value to skip testing the other half
        self.stop = False                # boolean value to abruptly stop the binary_search
        self.nr_estimated_infected = 0   # estimated number of infected people based on the upper and lower bound
        self.connectivity_degree = 0.0   # degree to which the graph is connected
        self.infection_degree = 0.0      # estimated ratio of infected nodes and all nodes in the graph

    # resets the specifics
    def reset(self):
        self.graph.nodes = []
        self.graph.edges = []
        self.graph.node_indices = []
        self.infected = []
        self.nr_queries = 0
        self.stop = False
