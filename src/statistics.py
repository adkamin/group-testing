from graph import Graph

class Statistics:
    def __init__(self):
        self.graph = Graph()
        self.initially_infected = 0
        self.infection_chance = 0
        self.lower_bound = 0
        self.upper_bound = 0

    def __str__(self):
        return f'({self.graph} \n {self.initially_infected}, {self.infection_chance}, {self.lower_bound}, {self.upper_bound})'