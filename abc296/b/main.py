"""

"""

def main():
    alphabet = "abcdefgh"
    count = 8
    for i in range(1, 9):
        S = input()
        for j in range(8):
            if S[j] == "*":
                print(alphabet[j] + str(count))
        count -= 1


main()