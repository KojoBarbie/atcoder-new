"""

"""

def main():
    S = input()  # 文字列Sを受け取る
    N = int(input())  # 整数Nを受け取る

    T = set()  # Tを集合として初期化する
    for i in range(1 << S.count('?')):  # '?' の数だけ2進数を全探索する
        b = bin(i)[2:].zfill(S.count('?'))  # 2進数表記に変換し、0埋めして桁を合わせる
        t = S.replace('?', '{}').format(*b)  # '?' を 0 or 1 に置換して文字列を作成
        T.add(int(t, 2))  # 文字列を2進数から10進数に変換し、Tに追加する

    max_val = -1  # 最大値を初期化する
    for t in T:
        if t <= N and t > max_val:  # N以下で最大の値を更新する
            max_val = t

    print(max_val)  # 結果を出力する

main()