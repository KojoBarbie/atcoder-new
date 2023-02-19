"""

"""

import sys


def main():
    N, K = map(int, input().split())
    sets = set(map(int, input().split()))
    result = 0

    for i in range(K):
        if i in sets:
            continue
        else:
            print(i)
            sys.exit()

    print(i + 1)


main()