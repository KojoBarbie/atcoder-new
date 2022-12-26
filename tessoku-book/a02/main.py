"""

"""

def main():
    N, X = map(int, input().split())
    array = list(map(int, input().split()))
    flag = False
    for key in array:
        if key == X:
            flag = True
    if flag:
        print("Yes")
    else:
        print("No")


main()