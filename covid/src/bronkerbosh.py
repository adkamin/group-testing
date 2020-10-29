from graph import Graph

def find_maximal_cliques(g):
    bron_kerbosh(g, g.nodes, [], [])
    
    
def bron_kerbosh(g, P, R, X):
    if len(set(P).union(X)) == 0:
        print(f'Found a maximal clique: {R}')
    for v in P:
        neighbors = g.find_neighbors(v)
        bron_kerbosh(g, set(P).intersection(neighbors), set(R).union([v]), set(X).intersection(neighbors))
        P = [i for i in P if i != v]
        X = set(X).union([v])