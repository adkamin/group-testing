from algorithm import find_candidates
import sys


def main():
    number_of_tests = int(input())
    while number_of_tests > 0:
        candidates = find_candidates()
        s = str(candidates)
        s = s.replace('[', '').replace(']', '').replace(',', '')
        print("answer " + s)
        server_reply = input()
        print(server_reply, file=sys.stderr)
        number_of_tests -= 1


if __name__ == '__main__':
    main()

