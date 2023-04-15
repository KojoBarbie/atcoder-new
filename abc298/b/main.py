"""

"""
import sys

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        array = list(map(int, input().split()))
        A.append(array)
    for i in range(N):
        array = list(map(int, input().split()))
        B.append(array)

    for i in range(4):
        flag = True
        for j in range(N):
            for k in range(N):
                if A[j][k] == 1 and B[j][k] != 1:
                    flag = False
        if flag:
            print("Yes")
            sys.exit()
        else:
            C = [[0] * N for l in range(N)]
            for l in range(N):
                for m in range(N):
                    C[N - 1 - m][l] = A[l][m]
            A = C
    print("No")


main()