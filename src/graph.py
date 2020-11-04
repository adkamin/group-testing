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

    def find_maximal_cliques(self):
        nodes = list(range(len(self.nodes)))
        self.bron_kerbosh(nodes, [], [])
        for i in self.cliques:
            print(i)
    
    def bron_kerbosh(self, P, R, X):
        if len(set(P).union(X)) == 0:
            self.cliques.append(Clique(R, self.nodes))
            # TODO for every node in clique increment node.nr_cliques
        for v in P:
            neighbors = self.nodes[v].find_neighbors(self.edges)
            self.bron_kerbosh(set(P).intersection(neighbors), set(R).union([v]), set(X).intersection(neighbors))
            P = [i for i in P if i != v]
            X = set(X).union([v])

    # TODO method to sort by weight
    def sort_cliques(self):
        # sorted(self.cliques, lambda clique : clique.weight)
        pass


class Node:
    def __init__(self, i, graph):
        self.index = i
        self.neighbors = self.find_neighbors(graph.edges)
        self.degree = len(self.neighbors)
        self.nr_cliques = 0
        self.infected = False
        self.init_infected = False

    def find_neighbors(self, edges):
        return [edge[(edge.index(self.index) + 1) % 2] for edge in edges if self.index in edge]

    def __str__(self):
        return f'{self.index}, {self.neighbors}, {self.degree}'


class Clique:
    def __init__(self, nodes, actual_nodes):  # TODO find a way to turn indices into nodes
        self.nodes = nodes
        self.size = len(nodes)  # I think we will still need this
        self.weight = self.find_degree(actual_nodes) + self.size

    def find_degree(self, actual_nodes):
        sum = 0
        for node in self.nodes:
            sum += actual_nodes[node].degree - (self.size - 1)
        return sum

    def __str__(self):
        return f'({self.nodes}, {self.weight})'

            


