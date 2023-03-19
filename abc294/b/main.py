"""

"""

def main():
    H, W= map(int, input().split())
    alphabet = [0, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in range(H):
        S = ""
        array = list(map(int, input().split()))
        for num in array:
            if num == 0:
                S = S + "."
            else:
                S = S + alphabet[num]
        print(S)


main()