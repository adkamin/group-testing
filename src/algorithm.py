from specifics import Specifics
import sys

specs = Specifics()  # statistics to store necessary information for the algorithm


# returns the final list of nodes which were found to be infected
def find_candidates():
    specs = store_specs()
    specs.infected = []
    if specs.infection_degree > 0.5 or (specs.connectivity_degree > 0.18 and specs.infection_degree > 0.25):
        individual_testing()
    else:
        binary_testing()
    print("Number of queries: " + str(specs.nr_tests), file=sys.stderr)
    return specs.infected


# stores the data from the server into a graph object
def store_specs():  # TODO call this save_statistics()?
    specs.reset()
    nr_nodes = int(input())
    specs.graph.node_indices = list(range(nr_nodes))
    print("\nNumber of nodes: " + str(nr_nodes), file=sys.stderr)
    nr_edges = int(input())
    specs.nr_initially_infected = int(input())
    input()  # we do not make use of infection chance p
    bounds = input().split(' ')
    specs.lower_bound = int(bounds[0])
    specs.upper_bound = int(bounds[1])
    specs.nr_estimated_infected = (specs.upper_bound + specs.lower_bound) / 2
    most_edges = (nr_nodes*(nr_nodes - 1)) / 2
    specs.connectivity_degree = nr_edges/most_edges
    specs.infection_degree = specs.nr_estimated_infected / nr_nodes
    create_edges(nr_edges)
    specs.graph.create_nodes()
    return specs


# creates tuples of nodes which form an edge and stores it into specs.graph
def create_edges(nr_edges):
    while nr_edges > 0:
        edge = input().split(' ')
        specs.graph.edges.append((int(edge[0]), int(edge[1])))
        nr_edges -= 1


# tests the nodes individually
def individual_testing():
    nodes = specs.graph.sort_by_degree(specs.graph.node_indices)
    print("Binary search was avoided", file=sys.stderr)
    for node in nodes:
        if len(specs.infected) >= specs.upper_bound:
            return
        if run_test(node):
            specs.infected.append(node)


# tests the nodes with binary search
def binary_testing():
    sub_graphs = connected_tuples(specs.graph.edges)
    isolated_nodes = specs.graph.get_isolated_nodes()
    if len(isolated_nodes) > 0:
        sub_graphs.add(tuple(isolated_nodes))
    for graph in sub_graphs:
        sorted_graph = specs.graph.sort_by_degree(graph)
        n = round(len(sorted_graph) / (specs.nr_estimated_infected * (len(graph) / len(specs.graph.nodes))))
        sorted_graph = [sorted_graph[i * n:(i + 1) * n] for i in range((len(sorted_graph) + n - 1) // n)]
        for lst in sorted_graph:
            binary_search(lst, False)
    if len(specs.graph.edges) == 1:
        sorted_nodes = specs.graph.sort_by_degree(specs.graph.node_indices)
        n = round(len(sorted_nodes) / specs.nr_estimated_infected)
        sorted_nodes = [sorted_nodes[i * n:(i + 1) * n] for i in range((len(sorted_nodes) + n - 1) // n)]
        for lst in sorted_nodes:
            binary_search(lst, False)


# searches for positive nodes in binary search fashion, stores the intermediate results into specs.positive
def binary_search(nodes, left_half):
    nodes = specs.graph.sort_by_degree(nodes)
    skip = (specs.lower_bound - (len(specs.graph.nodes) - len(nodes) - len(specs.infected))) > 0
    if len(specs.infected) >= specs.upper_bound or (specs.connectivity_degree == 0 and len(specs.infected) >= specs.nr_initially_infected):
        return
    if len(nodes) > 1:  # i.e. case group
        if skip or specs.skip_test or run_test(nodes):
            specs.skip_test = False
            new_list_1, new_list_2 = divide_in_half(nodes)
            binary_search(new_list_1, True)
            binary_search(new_list_2, False)
        else:
            specs.graph.update_graph(nodes)
            specs.skip_test = left_half
    elif len(nodes) == 1:  # i.e. case node
        if skip or specs.skip_test or run_test(nodes):  # list is not really a list anymore but more of a singleton
            specs.skip_test = False
            specs.infected.append(nodes[0])
            specs.graph.update_graph(nodes)
        else:
            specs.graph.update_graph(nodes)
            specs.skip_test = left_half


# TODO Stolen from stack overflow
def connected_tuples(pairs):
    # for every element, we keep a reference to the list it belongs to
    lists_by_element = {}

    def make_new_list_for(x, y):
        lists_by_element[x] = lists_by_element[y] = [x, y]

    def add_element_to_list(lst, el):
        lst.append(el)
        lists_by_element[el] = lst

    def merge_lists(lst1, lst2):
        merged_list = lst1 + lst2
        for el in merged_list:
            lists_by_element[el] = merged_list

    for x, y in pairs:
        xList = lists_by_element.get(x)
        yList = lists_by_element.get(y)
        if not xList and not yList:
            make_new_list_for(x, y)
        if xList and not yList:
            add_element_to_list(xList, y)
        if yList and not xList:
            add_element_to_list(yList, x)
        if xList and yList and xList != yList:
            merge_lists(xList, yList)
    # return the unique lists present in the dictionary
    # print("Groups: " + str(set(tuple(l) for l in lists_by_element.values())), file=sys.stderr)
    return set(tuple(l) for l in lists_by_element.values())


# divides binary_nodes into halves
def divide_in_half(binary_nodes):
    half = len(binary_nodes) // 2
    return binary_nodes[:half], binary_nodes[half:]


# returns true if test was positive, returns false otherwise
def run_test(candidates):
    specs.nr_tests += 1
    print("test", *candidates)
    server_reply = input()
    return server_reply == "true"


