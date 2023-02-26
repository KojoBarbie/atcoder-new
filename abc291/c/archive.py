"""

"""

import sys
import numpy as np


def main():
    N = int(input())
    S = input()
    array = [[0] * (2 * N + 1) for i in range(2 * N + 1)]

    T = [N + 1, N + 1]
    array[N + 1][N + 1] = 1
    for j in range(len(S)):
        if S[j] == "R":
            T[0] += 1
        elif S[j] == "L":
            T[0] -= 1
        elif S[j] == "U":
            T[1] += 1
        else:
            T[1] -= 1

        if array[T[0]][T[1]] == 0:
            array[T[0]][T[1]] += 1
        else:
            print("Yes")
            sys.exit()

    print("No")


main()
