from statistics import Statistics
import sys

stats = Statistics()


# returns the final list of nodes which were found to be positive
def find_candidates():
    stats = read_graph()
    stats.positive = []
    sorted_nodes = stats.graph.sort_by_degree(stats.graph.node_indices)  # list of nodes sorted by degree
    # stolen from Geeks for Geeks
    n = int(len(sorted_nodes)/((stats.upper_bound+stats.lower_bound)/2))
    sorted_nodes = [sorted_nodes[i*n:(i+1)*n] for i in range((len(sorted_nodes) + n-1) // n)]
    for lst in sorted_nodes:
        binary_search(lst, False)
    print("nr tests: " + str(stats.nr_tests), file=sys.stderr)
    return stats.positive


# stores the data from the server into a graph object
def read_graph():
    stats.graph.nodes = []
    stats.graph.edges = []
    stats.graph.node_indices = []
    stats.nr_tests = 0
    nodes = list(range(int(input())))
    print("\nnr nodes: " + str(len(nodes)), file=sys.stderr)
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


# searches for positive nodes in binary search fashion, stores the intermediate results into stats.positive
def binary_search(binary_nodes, left_half):
    binary_nodes = stats.graph.sort_by_degree(binary_nodes)
    # skip = (stats.lower_bound - (len(stats.graph.nodes) - len(binary_nodes) - len(stats.positive))) > 0
    # if skip:
    #     print("Woa It happend!!", file=sys.stderr)
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
            neighbors = stats.graph.nodes[binary_nodes[0]].neighbors  # get a list of all the neighbors of some node
            update_graph(binary_nodes)
            # TODO if we have time leftover take care of the clusters and neighbors
            # print(f'neighbors:{neighbors}', file=sys.stderr)
            # when this is the case then it means we just found a positive node and we dont know anything about
            # the neighbors yet. so we can increase the number of known clusters,
            # because this is the first node that we found from that cluster
            #    stats.cluster_count += 1
            if False and stats.infection_chance >= 0.5:
                print("Neighbor time!!!", file=sys.stderr)
                binary_search(neighbors, False)  # we keep on expanding the cluster
        else:
            update_graph(binary_nodes)
            stats.skip_test = left_half


# removes nodes_to_remove from stats.graph
def update_graph(nodes_to_remove):
    stats.graph.remove_nodes(nodes_to_remove)


# divides binary_nodes into halves
def divide_in_half(binary_nodes):
    half = len(binary_nodes) // 2
    return binary_nodes[:half], binary_nodes[half:]


# returns true if test was positive, returns false otherwise
def run_test(candidates):
    stats.nr_tests += 1
    s = str(candidates)
    s = s.replace('[', '').replace(']', '').replace(',', '')
    print(f'test {s}')
    # print("testing: " + s, file=sys.stderr)
    server_reply = input()
    # print(stats.graph.node_indices, file=sys.stderr)
    # print("server reply " + server_reply + "\n", file=sys.stderr)
    return server_reply == "true"


