"""

"""

import collections


def main():
    N = int(input())
    array = list(map(int, input().split()))
    count = 0

    result = [v for k, v in collections.Counter(array).items() if v > 1]
    for num in result:
        count += num // 2
    
    print(count)


main()