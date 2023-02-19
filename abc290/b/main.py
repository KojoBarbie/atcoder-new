"""

"""

def main():
    N, K = map(int, input().split())
    S = input()
    count = 0
    result = ""

    for i in range(N):
        if count >= K:
            result = result + "x"
        else:
            if S[i] == "o":
                result = result + "o"
                count += 1
            else:
                result = result + "x"

    print(result)





main()