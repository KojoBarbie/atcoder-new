"""

"""

import sys


def main():
    S = input()
    for i in range(len(S)):
        if S[i].isupper() == True:
            print(i + 1)
            sys.exit()


main()