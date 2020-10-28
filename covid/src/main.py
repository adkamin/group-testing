from graph import *


def main():
    # Read file and save into list of doubles
    with open("src/input", 'r') as inputfile:
        lst = inputfile.read()
        lst = [float(i) for i in lst.split()]

    # Create graph from the list
    g = Graph()
    g.nodes = list(range(int(lst[0])))
    index = 5
    for i in range(int(lst[1])):
        edge = (lst[index],lst[index+1])
        g.edges.append(edge)
        index += 2
    print(g.edges)
    print(g.nodes)


if __name__ == '__main__':
    main()
