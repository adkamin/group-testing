from specifics import Specifics
import sys

specs = Specifics()  # statistics to store necessary information for the algorithm


# returns the final list of nodes which were found to be infected
# complexity: O(O(individual_testing))
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
# O(O(create_edges))
def store_specs():
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
# complexity: O(nr_edges)
def create_edges(nr_edges):
    while nr_edges > 0:
        edge = input().split(' ')
        specs.graph.edges.append((int(edge[0]), int(edge[1])))
        nr_edges -= 1


# tests the nodes individually
# complexity: O(len(node_indices))
def individual_testing():
    nodes = specs.graph.sort_by_degree(specs.graph.node_indices)
    print("Binary search was avoided", file=sys.stderr)
    for node in nodes:
        if len(specs.infected) >= specs.upper_bound:
            return
        if run_test([node]):
            specs.infected.append(node)


# tests the nodes with binary search
# complexity: O(len(components)*O(binary_search))
def binary_testing():
    components = find_components()
    if len(specs.graph.edges) > 0: # case: graph is not disconnected
        for graph in components:
            sorted_graph = specs.graph.sort_by_degree(graph)
            n = round(len(sorted_graph) / (specs.nr_estimated_infected * (len(graph) / len(specs.graph.nodes))))
            sorted_graph = [sorted_graph[i * n:(i + 1) * n] for i in range((len(sorted_graph) + n - 1) // n)]
            for lst in sorted_graph:
                binary_search(lst, False)
    else: # case: graph is disconnected
        sorted_nodes = specs.graph.sort_by_degree(specs.graph.node_indices)
        n = round(len(sorted_nodes) / specs.nr_estimated_infected)
        sorted_nodes = [sorted_nodes[i * n:(i + 1) * n] for i in range((len(sorted_nodes) + n - 1) // n)]
        for lst in sorted_nodes:
            binary_search(lst, False)


# searches for positive nodes in binary search fashion, stores the intermediate results into specs.positive
# O(n/3 * 5)
# Same complexity as DFS: O(|V| + |E|)
def binary_search(nodes, left_half):
    if specs.stop: # base case 1
        return
    if len(specs.infected) >= specs.upper_bound: # base case 2
        return
    if specs.connectivity_degree == 0 and len(specs.infected) >= specs.nr_initially_infected: # base case 3
        return
    if len(specs.graph.node_indices) <= (specs.lower_bound - len(specs.infected)): # base case 4
        specs.stop = True
        specs.infected += specs.graph.node_indices
        return
    nodes = specs.graph.sort_by_degree(nodes)
    skip_lowerbound = (specs.lower_bound - (len(specs.graph.nodes) - len(nodes) - len(specs.infected))) > 0
    if len(nodes) > 1:  # case: group
        if skip_lowerbound or specs.skip_lefthalf or run_test(nodes):
            specs.skip_lefthalf = False
            new_list_1, new_list_2 = divide_in_half(nodes)
            binary_search(new_list_1, True)
            binary_search(new_list_2, False)
        else:
            specs.graph.update_graph(nodes)
            specs.skip_lefthalf = left_half
    elif len(nodes) == 1:  # case: node
        if skip_lowerbound or specs.skip_lefthalf or run_test(nodes):  # list is not really a list anymore but more of a singleton
            specs.skip_lefthalf = False
            specs.infected.append(nodes[0])
            specs.graph.update_graph(nodes)
        else:
            specs.graph.update_graph(nodes)
            specs.skip_lefthalf = left_half


# returns a list of connected components and a list of leftover isolated nodes
# complexity: O(len(edges)*len(node_indices))
def find_components():
    component_list = {}
    for node1, node2 in specs.graph.edges:
        list1 = component_list.get(node1) # O(len(component_list))
        list2 = component_list.get(node2) # O(len(component_list))
        if list1 and list2 and list1 != list2:
            combined_list = list1 + list2
            for node in combined_list: # O(2)
                component_list[node] = combined_list
        if list1 and not list2:
            list1.append(node2)
            component_list[node2] = list1
        if list2 and not list1:
            list2.append(node1)
            component_list[node1] = list2
        if not list1 and not list2:
            component_list[node1] = component_list[node2] = [node1, node2]
    components = set(tuple(l) for l in component_list.values()) 
    isolated_nodes = specs.graph.get_isolated_nodes() # O(len(node_indices))
    if len(isolated_nodes) > 0:
        components.add(tuple(isolated_nodes))
    return components



# divides nodes into halves
# complexity: O(len(nodes))
def divide_in_half(nodes):
    half = len(nodes) // 2
    return nodes[:half], nodes[half:]


# returns true if test was positive, returns false otherwise
# complexity: O(1)
def run_test(candidates):
    specs.nr_tests += 1
    print("test", *candidates)
    server_reply = input()
    return server_reply == "true"


