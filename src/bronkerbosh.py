from graph import Graph


def find_maximal_cliques(g):
    nodes = list(range(len(g.nodes)))
    bron_kerbosh(g, nodes, [], [])

    
def bron_kerbosh(g, P, R, X):
    if len(set(P).union(X)) == 0:
        print(f'Found a maximal clique: {R}')
        # TODO for every node in clique increment node.nr_cliques
    for v in P:
        neighbors = g.nodes[v].find_neighbors(g.edges)
        bron_kerbosh(g, set(P).intersection(neighbors), set(R).union([v]), set(X).intersection(neighbors))
        P = [i for i in P if i != v]
        X = set(X).union([v])