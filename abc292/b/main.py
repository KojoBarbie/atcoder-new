"""

"""

def main():
    N, Q= map(int, input().split())
    array = [0] * (N + 1)
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            array[x] += 1
        elif c == 2:
            array[x] += 2
        else:
            if array[x] >= 2:
                print("Yes")
            else:
                print("No")


main()