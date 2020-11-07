import sys

class Graph:
    def __init__(self):
        self.nodes = []
        self.node_indices = []
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

    def sort_by_degree(self, nodes_to_consider):
        self.node_indices = sorted(self.node_indices, key=lambda x : self.nodes[x].degree)

        # we don't want to return all the node_indices but only the ones that we are considering for the current binary search
        return [node_index for node_index in self.node_indices if node_index in nodes_to_consider]

    def remove_nodes(self, nodes_to_remove):
        for node_index in nodes_to_remove:
            neighbors = self.nodes[node_index].neighbors
            for neighbor in neighbors:
                self.nodes[neighbor].remove_neighbor(node_index)


class Node:
    def __init__(self, i, graph):
        self.index = i
        self.neighbors = self.find_neighbors(graph.edges)
        self.degree = len(self.neighbors)

    def find_neighbors(self, edges):
        return [edge[(edge.index(self.index) + 1) % 2] for edge in edges if self.index in edge]

    def remove_neighbor(self, neighbor_to_remove):
        self.neighbors.remove(neighbor_to_remove)
        self.degree -= 1

    def __str__(self):
        return f'{self.index}, {self.neighbors}, {self.degree}'

            


