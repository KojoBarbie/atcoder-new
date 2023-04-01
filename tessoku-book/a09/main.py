"""

"""

def main():
    H, W, N = map(int, input().split())

    array = [[0] * (W + 2) for i in range(H + 2)]
    for i in range(N):
        A, B, C, D = map(int, input().split())
        array[A][B] += 1
        array[C + 1][D + 1] += 1
        array[A][D + 1] -= 1
        array[C + 1][B] -= 1

    ruiseki_array = [[0] * (W + 1) for i in range(H + 1)]
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            ruiseki_array[i][j] = ruiseki_array[i][j - 1] + array[i][j]

    for j in range(1, W + 1):
        for i in range(1, H + 1):
            ruiseki_array[i][j] = ruiseki_array[i - 1][j] + ruiseki_array[i][j]

    for i in range(1, H + 1):
        for j in range(1, W):
            print(ruiseki_array[i][j], end=" ")
        print(ruiseki_array[i][W])


main()