"""

"""

def main():
    N, M, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Aを昇順ソート
    A.sort()
    # Bを昇順ソート
    B.sort()

    max_value = -1

    # Aの最小値を選んだ場合から順に考える
    for a in A:
        # aを選んだ場合のBの候補を求める
        candidates = [b for b in B if b <= a + D]
        if candidates:
            # Bの最大値を選んだ場合の贈り物の価値の和を計算し、最大値を更新する
            max_value = max(max_value, a + max(candidates))

    print(max_value)

main()