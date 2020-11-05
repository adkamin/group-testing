from statistics import Statistics

stats = Statistics()


def find_candidates():
    stats = read_graph()
    sorted_nodes = stats.dynamic_graph.sort_by_degree()          # list of nodes sorted by degree
    binary_search(sorted_nodes)
    return stats.positive


def read_graph():
    nodes = list(range(int(input())))
    number_of_edges = int(input())
    stats.initially_infected = int(input())
    stats.infection_chance = float(input())
    bounds = input().split(' ')
    stats.lower_bound = int(bounds[0])
    stats.upper_bound = int(bounds[1])
    while number_of_edges > 0:
        edge = input().split(' ')
        stats.graph.edges.append((int(edge[0]), int(edge[1])))
        number_of_edges -= 1
    stats.graph.create_nodes(nodes)
    stats.dynamic_graph = stats.graph
    return stats


def binary_search(list): # passing list of nodes/groups that need to be tested. We can also call this DFS?
    list = stats.dynamic_graph.sort_by_degree()
    if len(stats.dynamic_graph.nodes) < 1 or len(stats.positive) < stats.upperbound: #OR #clusters < i
        return
    if len(list) > 1:  # i.e. case group
        if run_test(list):
            new_list_1, new_list_2 = divide_in_half(list)
            binary_search(new_list_1)
            binary_search(new_list_2)
        else:
            update_graph(list)
    elif len(list) == 1:  # i.e. case node
        if run_test(list):  # list is not really a list anymore but more of a singleton
            stats.positive.append(list[0])
            neighbors = stats.dynamic_graph.nodes[list[0]].neighbors  # get a list of all the neighbors of some node
            update_graph(list)
            # TODO if we have time leftover take care of the clusters and neighbors
            # when this is the case then it means we just found a positive node and we dont know anything about
            # the neighbors yet. so we can increase the number of known clusters, because this is the first node that we found from that cluster
            #    stats.cluster_count += 1
            binary_search(neighbors)  # we keep on expanding the cluster
        else:
            update_graph(list)


# removes nodes_to_remove from stats.dynamic_graph and sorted_nodes, updates degrees
def update_graph(nodes_to_remove):
    for node_index in nodes_to_remove:
        for node in stats.dynamic_graph.nodes:
            if node_index == node.index:
                stats.dynamic_graph.remove(node)


def divide_in_half(list):
    half = len(list) // 2
    return list[:half], list[half:]


# returns true if test was positive returns false if test was negative
def run_test(candidates):
    s = str(candidates)
    s = s.replace('[', '').replace(']', '').replace(',', '')
    print(f'test {s}')
    server_reply = input()
    return bool(server_reply.capitalize())


# For testing purposes to read from input file
# def read_graph_input(input_file):
#     with open(input_file, 'r') as input_file:
#         number_of_tests = int(input_file.readline())
#         while number_of_tests > 0:
#             stats = Statistics()
#             nodes = list(range(int(input_file.readline())))
#             number_of_edges = int(input_file.readline())
#             stats.initially_infected = int(input_file.readline())
#             stats.infection_chance = float(input_file.readline())
#             bounds = input_file.readline().split(' ')
#             stats.lower_bound = int(bounds[0])
#             stats.upper_bound = int(bounds[1])
#             while number_of_edges > 0:
#                 edge = input_file.readline().split(' ')
#                 stats.graph.edges.append((int(edge[0]), int(edge[1])))
#                 number_of_edges -= 1
#             stats.graph.create_nodes(nodes)
#             number_of_tests -= 1
#             stats.graph.find_maximal_cliques()
#             break

