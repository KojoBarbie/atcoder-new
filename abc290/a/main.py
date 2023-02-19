"""

"""

def main():
    M, N = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0
    for key in B:
        result += A[key - 1]
    
    print(result)


main()