"""

"""

def main():
    N = int(input())
    S = input()
    result = ""

    if S.count("A") == S.count("T"):
        if S[-1] == "A":
            result = "T"
        else:
            result = "A"
    elif S.count("A") > S.count("T"):
        result = "A"
    else:
        result = "T"
    print(result)


main()