"""

"""

import sys


def main():
    N, X = map(int, input().split())
    array = set(map(int, input().split()))

    for num in array:
        result = num - X
        if result in array:
            print("Yes")
            sys.exit()

    print("No")


main()