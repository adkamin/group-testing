from statistics import Statistics
import sys

stats = Statistics()


# returns the final list of nodes which were found to be positive
def find_candidates():
    stats = read_graph()
    # for node in stats.graph.nodes:
        # print(f'{node.degree}, {node.secondary_degree}', file=sys.stderr)
    print(f'info: connectivity_degree={stats.connectivity_degree}, infection_degree={stats.infection_degree}, infection_chance={stats.infection_chance}', file=sys.stderr)
    stats.positive = []
    sub_graphs = connected_tuples(stats.graph.edges)
    isolated_nodes = stats.graph.get_isolated_nodes()
    if len(isolated_nodes) > 0:
        sub_graphs.add(tuple(isolated_nodes))
    
    # for g in sub_graphs:
    #     count += len(g)
    
    # print(f"{count}, {len(stats.graph.node_indices)}", file=sys.stderr)

    if (len(stats.graph.nodes)/2) < stats.estimated_infected or (stats.connectivity_degree > 0.18 and stats.infection_degree > 0.25):
        nodes = stats.graph.sort_by_degree(stats.graph.node_indices)
        print("better don't do binary search ", file=sys.stderr)
        for node in nodes:
            if len(stats.positive) >= stats.upper_bound:
                return
            if run_test(node):
                stats.positive.append(node)
    else:
        for graph in sub_graphs:
            sorted_graph = stats.graph.sort_by_degree(graph)
            n = round(len(sorted_graph) / (stats.estimated_infected * (len(graph) / len(stats.graph.nodes))))
            sorted_graph = [sorted_graph[i * n:(i + 1) * n] for i in range((len(sorted_graph) + n - 1) // n)]
            for lst in sorted_graph:
                binary_search(lst, False)
        if len(stats.graph.edges) == 1:
            # stolen from Geeks for Geeks
            sorted_nodes = stats.graph.sort_by_degree(stats.graph.node_indices)  # list of nodes sorted by degree
            n = round(len(sorted_nodes) / stats.estimated_infected)
            sorted_nodes = [sorted_nodes[i * n:(i + 1) * n] for i in range((len(sorted_nodes) + n - 1) // n)]
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
    stats.cluster_count = 0
    nodes = list(range(int(input())))
    print("\nnr nodes: " + str(len(nodes)), file=sys.stderr)
    number_of_edges = int(input())
    # print("nr edges: " + str(number_of_edges) + "\n", file=sys.stderr)
    stats.initially_infected = int(input())
    stats.infection_chance = float(input())
    bounds = input().split(' ')
    stats.lower_bound = int(bounds[0])
    stats.upper_bound = int(bounds[1])
    stats.estimated_infected = (stats.upper_bound+stats.lower_bound)/2
    most_edges = (len(nodes)*(len(nodes)-1))/2
    stats.connectivity_degree =  number_of_edges/most_edges
    stats.infection_degree = stats.estimated_infected/len(nodes)
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
    skip = (stats.lower_bound - (len(stats.graph.nodes) - len(binary_nodes) - len(stats.positive))) > 0
    if len(stats.positive) >= stats.upper_bound or (stats.connectivity_degree == 0 and len(stats.positive) >= stats.initially_infected):
        return
    if len(binary_nodes) > 1:  # i.e. case group
        if skip or stats.skip_test or run_test(binary_nodes):
            stats.skip_test = False
            new_list_1, new_list_2 = divide_in_half(binary_nodes)
            binary_search(new_list_1, True)
            binary_search(new_list_2, False)
        else:
            update_graph(binary_nodes)
            stats.skip_test = left_half
    elif len(binary_nodes) == 1:  # i.e. case node
        if skip or stats.skip_test or run_test(binary_nodes):  # list is not really a list anymore but more of a singleton
            stats.skip_test = False
            stats.positive.append(binary_nodes[0])
            update_graph(binary_nodes)
        else:
            update_graph(binary_nodes)
            stats.skip_test = left_half

# Stolen from stack overflow
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


