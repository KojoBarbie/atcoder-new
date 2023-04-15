"""

"""
import sys

def main():
    N = int(input())
    S = input()
    flag = False
    for i in range(len(S)):
        if S[i] == "x":
            print("No")
            sys.exit()
        elif S[i] == "o":
            flag = True
    
    if flag:
        print("Yes")
    else:
        print("No")


main()