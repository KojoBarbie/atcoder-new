"""

"""

def main():
    N = int(input())
    array = list(map(int, input().split()))

    result = []
    for i in range(len(array) - 1):
        num = array[i]
        if abs(num - array[i + 1]) <= 1:
            result.append(num)
        elif num - array[i + 1] >= 2:
            while num > array[i + 1]:
                result.append(num)
                num -= 1
        else:
            while num < array[i + 1]:
                result.append(num)
                num += 1
    result.append(array[-1])
    print(*result)


main()