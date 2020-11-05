from statistics import Statistics

stats = Statistics() # TODO If this is possible, we don't need to keep passing stats to every function

def find_candidates():
    stats = read_graph()
    stats.graph.find_maximal_cliques()
    stats.graph.sort_cliques()
    # Test the isolated nodes and find candidates (here or at the end)
    find_isolated_candidates()
    while not stats.unknown.empty or len(stats.positive) < stats.upperbound:  # while still nodes to be tested
        # TODO we need a way to find isolated cliques of size k > 4, call this group "cliques"
        # binary_search(cliques)
        # TODO cliques of size >= 4 are seen as nodes, call this "nodes"
        # binary_search(nodes)
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
    return stats


def find_isolated_candidates():
    isolated_candidates = []
    for clique in stats.graph.cliques:         # TODO I'm sure you ca do this in one line :P
        if clique.weight = 1:                  # why this error? 
            isolated_candidates.append(clique)
    binary_search(isolated_candidates)


def binary_search(list): # passing list of nodes/groups that need to be tested. We can also call this DFS?
    # TODO This is 4c basically. Divide and test, update stats.positive, stats.negative, stats.unknown, repeat
    # TODO When testing individual nodes, search for clusters
    # TODO Keep in mind they want us to send tests in bulk :(

    # if !unknown.empty(still nodes to be tested) OR len(positive) < upperbound OR #clusters < i
        # get out of here + get out of the while loop
    
    if len(list) > 1: # i.e. case group
        if run_test(list):
            new_list_1, new_list_2 = divide_in_half(list) # TODO write function that divides list in half
            binary_search(new_list_1)
            binary_search(new_list_2)
        else:
            stats.negative += list
            stats.unknown -= list # should probably be something like intersect but im not sure
    elif len(list) == 1: # i.e. case node
        if run_test(list): # list is not really a list anymore but more of a singleton
            stats.positive.append(list[0])
            stats.unknown.remove(list[0])
            neighbors = get_neightbors(list[0]) # get a list of all the neighbors of some node
            if all neighbors in stats.unknown # when this is the case then it means we just found a positive node and we dont know anything about
            # the neighbors yet. so we can increase the number of known clusters, because this is the first node that we found from that cluster
                stats.cluster_count += 1
            for neighbor in neighbors: # we keep on expanding the cluster
                binary_search(neighbor)
        else:
            stats.negative.append(list[0])
            stats.unknown.remove(list[0])

    # idea: instead of all those stats.blabla.append lines we might want to introduce functions like stats.negative.add_negative(list) that would also
    # remove those elements from stats.unknown


    pass

def run_test(list): # TODO write function that runs a test, 
    # returns true if test was positive returns false if test was negative
    print(f'answer {list}') # TODO convert "list" into a string acceptable by server
    server_reply = input()
    return server_reply # TODO write function that turns string var into boolean var



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

