"""

"""

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = A + B
    C.sort()

    a_num, b_num = 0, 0
    a_result = []
    b_result = []

    for i in range(0, len(C)):
        if A[a_num] == C[i]:
            a_result.append(i + 1)
            a_num = a_num + 1 if a_num < N - 1 else a_num
        else:
            b_result.append(i + 1)
            b_num = b_num + 1 if b_num < M - 1 else b_num

    print(*a_result)
    print(*b_result)


main()