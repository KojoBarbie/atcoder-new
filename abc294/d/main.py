"""
解き切らなかった。(TLE)
"""

def main():
    N, Q = map(int, input().split())
    count = 1
    min_guest = 0
    waiting = set()

    for i in range(Q):
        event = input()
        if "2" in event:
            a, x = map(int, event.split())
            waiting.remove(x)
        elif event == "1":
            waiting.add(count)
            count += 1
        else:
            print(min(waiting))


main()