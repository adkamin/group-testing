from statistics import Statistics
from bronkerbosh import find_maximal_cliques

def IO(input_file):
    number_of_tests = int(input_file.readline())
    while number_of_tests > 0:
        stats = Statistics()
        stats.graph.nodes = list(range(int(input_file.readline())))
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
        number_of_tests -= 1
        print('finding cliques...')
        find_maximal_cliques(stats.graph)
        