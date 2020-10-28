from graph import *
from IO import IO



# def main():
#     # Read file and save into list of doubles
#     with open("src/input", 'r') as inputfile:
#         lst = inputfile.read()
#         lst = [float(i) for i in lst.split()]

#     # Create graph from the list
#     g = Graph()
#     g.nodes = list(range(int(lst[0])))
#     index = 5
#     for i in range(int(lst[1])):
#         edge = (lst[index],lst[index+1])
#         g.edges.append(edge)
#         index += 2
#     print(g.edges)
#     print(g.nodes)

def main():
    while True:
        try:
            # path = input("Please enter a input path:\n")
            path = "covid/src/input"
            with open(path, 'r') as input_file:
                IO(input_file)
                break
        except (FileNotFoundError, IOError):
            print("Error: file not found")
        else:
            break
        
    


if __name__ == '__main__':
    main()

