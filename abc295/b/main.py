"""

"""

def main():
    R, C = map(int, input().split())
    array = []
    for i in range(R):
        S = input()
        array.append(list(S))

    for j in range(1, 10):
        for k in range(R):
            for l in range(C):
                if array[k][l] == str(j):
                    array[k][l] = "."
                    for m in range(R):
                        for n in range(C):
                            if array[m][n] == "#" and abs(k - m) + abs(l - n) <= j:
                                array[m][n] = "."

    for key in array:
        print("".join(key))

main()