"""

"""

from collections import defaultdict

N = int(input())
Q = int(input())

cards = defaultdict(set)
boxes = defaultdict(list)

for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        cards[q[1]].add(q[2])
        boxes[q[2]].append(q[1])
    elif q[0] == 2:
        print(*sorted(boxes[q[1]]))
    else:
        print(*sorted(list(cards[q[1]])))
