"""

"""

def main():
    D = int(input())
    N = int(input())
    attendee = [0] * (D + 2)

    # 人数の増減を配列に記録
    for i in range(N):
        L, R = map(int, input().split())
        attendee[L] += 1
        attendee[R + 1] -= 1

    result = 0
    for j in range(1, len(attendee) - 1):
        result += attendee[j]
        print(result)


main()