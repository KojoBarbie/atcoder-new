"""

"""

def main():
    N = int(input())
    array = list(map(int, input().split()))
    array.sort()

    sumnum = sum(array[N: -N])
    print(sumnum / (3 * N))

main()