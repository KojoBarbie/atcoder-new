"""

"""

def main():
    H, W = map(int, input().split())
    for j in range(H):
        S = input() + "."
        result = [0] * (W + 1)

        for i in range(len(S)):
            if result[i] == "C":
                continue
            elif S[i] == "T" and S[i + 1] == "T":
                result[i] = "P"
                result[i + 1] = "C"
            else:
                result[i] = S[i]

        print("".join(result[0:W]))


main()