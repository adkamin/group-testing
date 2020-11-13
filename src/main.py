from algorithm import find_candidates
import sys


def main():
    nr_tests = int(input())
    while nr_tests > 0:
        candidates = find_candidates()
        print("answer", *candidates)
        server_reply = input()
        print(server_reply, file=sys.stderr)
        nr_tests -= 1


if __name__ == '__main__':
    main()

