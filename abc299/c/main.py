"""

"""

def find_positions(s, target):
    # targetが含まれている場合は、位置を格納する配列を用意する
    positions = [0]

    # 文字列s中にtargetが出現する位置を検索し、positionsに格納する
    start = 0
    while True:
        index = s.find(target, start)
        if index == -1:
            break
        positions.append(index)
        start = index + len(target) + 1

    return positions

def main():
    N = int(input())
    S = input()

    if not "o" in S or not "-" in S:
        print(-1)
    else:
        array = find_positions(S, "-")
        array.append(N + 1)
        result = 0
        for i in range(1, len(array)):
            result_i = array[i] - array[i - 1] - 1
            result = max(result, result_i)

        print(result)


main()