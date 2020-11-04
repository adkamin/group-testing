from statistics import Statistics


def IO(input_file):
    read_graph_input(input_file)
    # read_graph_server()


# For testing purposes
def read_graph_input(input_file):
    number_of_tests = int(input_file.readline())
    while number_of_tests > 0:
        stats = Statistics()
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
        stats.graph.create_nodes(nodes)
        number_of_tests -= 1
        stats.graph.find_maximal_cliques()
        break

# To communicate with the server
def read_graph_server():
    number_of_tests = int(input())
    while number_of_tests > 0:
        stats = Statistics()
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
        number_of_tests -= 1
        print("test 0")
        answer = input()
        print("answer 0")
        answer = input()