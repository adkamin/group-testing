from graph import Graph
from IO import IO


def main():
    # Code for testing with inputfile
    # while True:
    #     try:
    #         # path = input("Please enter a input path:\n")
    #         path = "src/input"
    #         with open(path, 'r') as input_file:
    #             IO(input_file)
    #             break
    #     except (FileNotFoundError, IOError):
    #         print("Error: file not found")
    #     else:
    #         break

    # Code for testing with server
    inputfile = "src/input" # dummy
    IO(inputfile)


if __name__ == '__main__':
    main()

