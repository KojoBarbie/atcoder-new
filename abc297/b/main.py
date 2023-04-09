"""

"""

import sys


def main():
    S = list(input())

    array_1 = [i for i, x in enumerate(S) if x == 'B']
    if sum(array_1) % 2 == 0:
        print("No")
        sys.exit()
    
    array_2 = [i for i, x in enumerate(S) if x == 'R']
    index_K = S.index("K")
    if array_2[0] <= index_K and array_2[1] >= index_K:
        print("Yes")
    else:
        print("No")


main()