"""
N = マスの数 = mod N（最後にNをわる）
D = 一回一回足すやつ
K = K番目に色を付けるものを答える
"""

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def main():
    T = int(input())
    for i in range(T):
        N, D, K = map(int, input().split())

        if K == 1:
            print(0)
            continue

        omg = gcd(N, D)
        if omg == 1:
            num = (K - 1) * D
            print(num % N)
        else:
            num = (K - 1) * D + (K - 1) // (N // omg)
            print(num % N)

main()