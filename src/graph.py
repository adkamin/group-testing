import sys


class Graph:
    def __init__(self):
        self.nodes = []         # nodes objects storing additional values such as neighbors and degree
        self.node_indices = []  # indices to access the nodes easily
        self.edges = []         # tuples of nodes that form an edge

    # given list of increasing indices, creates list of node objects and saves it into self.nodes
    def create_nodes(self, list):
        for node in list:
            self.nodes.append(Node(node, self))

    # sorts the nodes in increasing fashion
    def sort_by_degree(self, nodes_to_consider):
        return sorted(nodes_to_consider, key=lambda x: self.nodes[x].degree)

    # removes nodes_to_remove from the graph and updates their neighbors about this change
    # not sure if still needed
    def remove_nodes(self, nodes_to_remove):
        for node_index in nodes_to_remove:
            self.node_indices.remove(node_index)
            neighbors = self.nodes[node_index].neighbors
            for neighbor in neighbors:
                self.nodes[neighbor].remove_neighbor(node_index)

    # the function that we use that finds the subgraph of a graph does not consider isolated nodes, so we needed a seperate function for that
    def get_isolated_nodes(self):
        lst = [node_index for node_index in self.node_indices if self.nodes[node_index].degree == 0]
        return lst

class Node:
    def __init__(self, i, graph):
        self.index = i
        self.neighbors = self.find_neighbors(graph.edges)
        self.degree = len(self.neighbors)

    # returns list of neighbors of self using graph.edges
    def find_neighbors(self, edges):
        return [edge[(edge.index(self.index) + 1) % 2] for edge in edges if self.index in edge]

    # removes neighbor_to_remove from self.neighbors and updates self.degree accordingly
    def remove_neighbor(self, neighbor_to_remove):
        self.neighbors.remove(neighbor_to_remove)
        self.degree -= 1


            


