"""

"""

def main():
    H, W = map(int, input().split())
    C = [["."] * (W + 2)]
    for i in range(H):
        array = list(input())
        array.insert(0, ".")
        array.append(".")
        C.append(array)
    C.append(["."] * (W + 2))
    result = [0] * min(H, W)

    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if C[i][j] == "#":
                d = 0
                while True:
                    if C[i + d + 1][j + d + 1] == "#" and C[i + d + 1][j - d - 1] == "#" \
                        and C[i - d - 1][j + d + 1] == "#" and C[i - d - 1][j - d - 1] == "#":
                        d += 1
                    else:
                        if d != 0:
                            result[d - 1] += 1
                        break

    print(*result)


main()