from algorithm import find_candidates
import sys


# O(nr_problems * O(individual_testing))
def main():
    nr_problems = int(input())
    while nr_problems > 0:
        candidates = find_candidates()
        print("answer", *candidates)
        server_reply = input()
        print(server_reply, file=sys.stderr)
        nr_problems -= 1


if __name__ == '__main__':
    main()

