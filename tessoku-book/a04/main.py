"""
整数 N が 10 進法表記で与えられます。
N を 2 進法に変換した値を出力するプログラムを作成してください。
"""

def main():
    N = int(input())
    # 上の桁から順番に「2 進法に変換した値」を求める
    for x in [9,8,7,6,5,4,3,2,1,0]:
        wari = (2 ** x)
        print((N // wari) % 2, end='')

    print("")


main()