"""

"""

import sys

def main():
    Q = int(input())
    S = "1"
    head = 0
    MOD = 998244353

    input_data = sys.stdin.read().splitlines()

    for query in input_data:
        query = query.split()
        if query[0] == "1":
            S += query[1]
        elif query[0] == "2":
            head += 1
        else:
            num = int(S[head:]) % MOD
            print(num)

main()