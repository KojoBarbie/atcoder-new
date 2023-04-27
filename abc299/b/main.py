"""

"""

def main():
    N, T = map(int, input().split())
    C = list(map(int, input().split()))
    R = list(map(int, input().split()))

    if T in C:
        key = T
    else:
        key = C[0]

    result = 0
    player = 0
    for i in range(N):
        if C[i] == key and R[i] > result:
            result = R[i]
            player = i + 1

    print(player)


main()