"""

"""

import sys


def main():
    N, D = map(int, input().split())
    array = list(map(int, input().split()))
    for i in range(len(array) - 1):
        if array[i + 1] - array[i] <= D:
            print(array[i + 1])
            sys.exit()

    print(-1)


main()