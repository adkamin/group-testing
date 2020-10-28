from statistics import Statistics

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
        print(stats)
        break


        # stats.lower_bound = int(input_file.read(1))
        # input.read(1)
        # stats.upper_bound = int(input_file.readline())
        