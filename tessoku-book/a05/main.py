"""
赤・青・白の 3 枚のカードがあります。
太郎君は、それぞれのカードに 1 以上 N 以下の整数を書かなければなりません。
3 枚のカードの合計を K にするような書き方は何通りありますか。
"""

def main():
    N, K = map(int, input().split())
    count = 0

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            num = K - i - j
            if num >= 1 and num <= N:
                count += 1

    print(count)


main()