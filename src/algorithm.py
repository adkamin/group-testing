from statistics import Statistics
import sys

stats = Statistics()


def find_candidates():
    stats = read_graph()
    stats.positive = []
    # stats = read_graph_debug("src/input")
    sorted_nodes = stats.graph.sort_by_degree(stats.graph.node_indices)          # list of nodes sorted by degree
    # TODO test graph with disconnected edges
    binary_search(sorted_nodes, False)
    return stats.positive


def read_graph():
    stats.graph.nodes = []
    stats.graph.edges = []
    stats.graph.node_indices = []
    nodes = list(range(int(input())))
    # print("nr nodes: " + str(len(nodes)) + "\n", file=sys.stderr)
    number_of_edges = int(input())
    # print("nr edges: " + str(number_of_edges) + "\n", file=sys.stderr)
    stats.initially_infected = int(input())
    stats.infection_chance = float(input())
    bounds = input().split(' ')
    stats.lower_bound = int(bounds[0])
    stats.upper_bound = int(bounds[1])
    # print("upper bound: " + str(stats.upper_bound) + "\n", file=sys.stderr)
    while number_of_edges > 0:
        edge = input().split(' ')
        stats.graph.edges.append((int(edge[0]), int(edge[1])))
        number_of_edges -= 1
    stats.graph.node_indices = nodes
    stats.graph.create_nodes(nodes)
    return stats


def binary_search(binary_nodes, left_half): # passing list of nodes/groups that need to be tested. We can also call this DFS?
    binary_nodes = stats.graph.sort_by_degree(binary_nodes)
    if len(stats.graph.nodes) < 1 or len(stats.positive) >= stats.upper_bound: #OR #clusters < i
        # print(f'{len(stats.graph.nodes)}, {len(stats.positive)}, {stats.upper_bound}')
        return
    if len(binary_nodes) > 1:  # i.e. case group
        if stats.skip_test or run_test(binary_nodes):
            stats.skip_test = False
            new_list_1, new_list_2 = divide_in_half(binary_nodes)
            binary_search(new_list_1, True)
            binary_search(new_list_2, False)
        else:
            update_graph(binary_nodes)
            stats.skip_test = left_half
    elif len(binary_nodes) == 1:  # i.e. case node
        if stats.skip_test or run_test(binary_nodes):  # list is not really a list anymore but more of a singleton
            stats.skip_test = False
            stats.positive.append(binary_nodes[0])
            update_graph(binary_nodes)
            # neighbors = stats.graph.nodes[binary_nodes[0]].neighbors  # get a list of all the neighbors of some node
            # print(f'neighbors: {neighbors}', file=sys.stderr)
            # print("currently positive: " + str(len(stats.positive)), file=sys.stderr)
            # TODO if we have time leftover take care of the clusters and neighbors
            # when this is the case then it means we just found a positive node and we dont know anything about
            # the neighbors yet. so we can increase the number of known clusters, because this is the first node that we found from that cluster
            #    stats.cluster_count += 1
            # binary_search(neighbors, False)  # we keep on expanding the cluster
        else:
            update_graph(binary_nodes)
            stats.skip_test = left_half


# removes nodes_to_remove from stats.graph and sorted_nodes, updates degrees
def update_graph(nodes_to_remove):
    stats.graph.remove_nodes(nodes_to_remove)

def divide_in_half(binary_nodes):
    half = len(binary_nodes) // 2
    return binary_nodes[:half], binary_nodes[half:]

# returns true if test was positive returns false if test was negative
def run_test(candidates):
    stats.nr_tests += 1
    print("nr tests: " + str(stats.nr_tests), file=sys.stderr)
    s = str(candidates)
    s = s.replace('[', '').replace(']', '').replace(',', '')
    print(f'test {s}')
    print("testing: " + s, file=sys.stderr)
    server_reply = input()

    print("server reply " + server_reply + "\n", file=sys.stderr)

    # return bool(server_reply.capitalize())
    # this didnt work ): because bool(str) returns True if len(str) > 0 and false otherwise
    if(server_reply.lower() == "true"):
        return True
    elif(server_reply.lower() == "false"):
        return False
    else:
        print("ooh no")


# For testing purposes to read from input file
def read_graph_debug(input_file):
    with open(input_file, 'r') as input_file:
        number_of_tests = int(input_file.readline())
        while number_of_tests > 0:
            nodes = list(range(int(input_file.readline())))
            number_of_edges = int(input_file.readline())
            stats.initially_infected = int(input_file.readline())
            stats.infection_chance = float(input_file.readline())
            bounds = input_file.readline().split(' ')
            stats.lower_bound = int(bounds[0])
            stats.upper_bound = int(bounds[1])
            while number_of_edges > 0:
                edge = input_file.readline().split(' ')
                stats.graph.edges.append((int(edge[0]), int(edge[1])))
                number_of_edges -= 1
            stats.graph.node_indices = []
            stats.graph.node_indices = nodes
            stats.graph.create_nodes(nodes)
            stats.graph = stats.graph
            return stats

