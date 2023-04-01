"""

"""
import sys


def make_divisors(n, N):
    i = 1
    while i*i <= n:
        if n % i == 0:
            if i != n // i:
                if i <= N and n // i <= N:
                    return True
            else:
                if i <= N:
                    return True
        i += 1
    return False

def main():
    N, M = map(int, input().split())
    if N ** 2 < M:
        print(-1)
    elif N ** 2 == M:
        print(M)
    else:
        for j in range(M, N ** 2 + 1):
            flag = make_divisors(j, N)
            if flag:
                print(j)
                sys.exit()


main()