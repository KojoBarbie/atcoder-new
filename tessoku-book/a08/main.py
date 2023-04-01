"""

"""

def main():
    H, W = map(int, input().split())
    array = []

    for i in range(H):
        row = list(map(int, input().split()))
        array.append(row)

    # 累積和をもとめる
    ruiseki_array = [[0] * (W + 1) for i in range(H + 1)]

    # まず横方向に足してから、縦に足す
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            ruiseki_array[i][j] = ruiseki_array[i][j - 1] + array[i - 1][j - 1]

    for j in range(1, W + 1):
        for i in range(1, H + 1):
            ruiseki_array[i][j] = ruiseki_array[i - 1][j] + ruiseki_array[i][j]

    Q = int(input())
    for i in range(Q):
        A, B, C, D = map(int, input().split())
        result = ruiseki_array[C][D] + ruiseki_array[A - 1][B - 1] \
               - ruiseki_array[A - 1][D] - ruiseki_array[C][B - 1]
        print(result)


main()