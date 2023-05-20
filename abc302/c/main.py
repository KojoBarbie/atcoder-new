"""

"""

import collections

def is_edit_distance_one(str1, str2):
    if len(str1) != len(str2):
        return False
    diff_count = 0
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            diff_count += 1
            if diff_count > 1:
                return False
    return diff_count == 1

def main():
    N, M = map(int, input().split())
    S = []
    for i in range(N):
        S_i = input()
        S.append(S_i)

    array = []
    for i in range(N):
        array_i = []
        for j in range(N):
            array_i.append(is_edit_distance_one(S[i], S[j]))
        c = collections.Counter(array_i)
        array.append(c[1])

    result = collections.Counter(array)
    if result[0] > 0 or result[1] > 2:
        print("No")
    else:
        print("Yes")



main()