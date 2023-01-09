"""
遊園地「ALGO-RESORT」では N 日間にわたるイベントが開催され、 i 日目 (1≤i≤N) には Ai 人が来場しました。

以下の合計 Q 個の質問に答えるプログラムを作成してください。
1 個目の質問：L1 日目から R1 日目までの合計来場者数は？
"""

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    array = [0]
    for num in range(N):
        array.append(A[num] + array[num])

    for i in range(Q):
        L, R = map(int, input().split())
        print(array[R] - array[L - 1])


main()