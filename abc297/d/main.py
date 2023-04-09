"""

"""

def main():
    a, b = map(int, input().split())
    A = max(a, b)
    B = min(a, b)
    count = 0
    while B > 0:
        count += A // B
        A, B = B, A % B
    print(count - 1)


main()