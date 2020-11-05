from algorithm import algorithm


def main():
    number_of_tests = int(input())
    while number_of_tests > 0:
        candidates = algorithm.find_candidates()    # TODO convert "candidates" into a string acceptable by server
        print("answer " + candidates)
        server_reply = input()
        number_of_tests -= 1


if __name__ == '__main__':
    main()

