"""

"""

import sys


def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S_i = list(input())
        S.append(S_i)

    # よこ
    for row in range(H):
        for col in range(W - 4):
            if S[row][col] == "s" and S[row][col + 1] == "n" and S[row][col + 2] == "u" and S[row][col + 3] == "k" and S[row][col + 4] == "e":
                    for n in range(5):
                        print(str(row + 1) + " " + str(col + 1 + n))
                    sys.exit()
            if S[row][col] == "e" and S[row][col + 1] == "k" and S[row][col + 2] == "u" and S[row][col + 3] == "n" and S[row][col + 4] == "s":
                    for n in range(5):
                        print(str(row + 1) + " " + str(col + 5 - n))
                    sys.exit()
    # たて
    for row in range(H - 4):
        for col in range(W):
                if S[row][col] == "s" and S[row + 1][col] == "n" and S[row + 2][col] == "u" and S[row + 3][col] == "k" and S[row + 4][col] == "e":
                    for n in range(5):
                        print(str(row + 1 + n) + " " + str(col + 1))
                    sys.exit()
                if S[row][col] == "e" and S[row + 1][col] == "k" and S[row + 2][col] == "u" and S[row + 3][col] == "n" and S[row + 4][col] == "s":
                    for n in range(5):
                        print(str(row + 5 - n) + " " + str(col + 1))
                    sys.exit()

    # ななめ
    for row in range(H - 4):
        for col in range(W - 4): 
                if S[row][col] == "s" and S[row + 1][col + 1] == "n" and S[row + 2][col + 2] == "u" and S[row + 3][col + 3] == "k" and S[row + 4][col + 4] == "e":
                    for n in range(5):
                        print(str(row + 1 + n) + " " + str(col + 1 + n))
                    sys.exit()
                if S[row][col] == "e" and S[row + 1][col + 1] == "k" and S[row + 2][col + 2] == "u" and S[row + 3][col + 3] == "n" and S[row + 4][col + 4] == "s":
                    for n in range(5):
                        print(str(row + 5 - n) + " " + str(col + 5 - n))
                    sys.exit()


main()