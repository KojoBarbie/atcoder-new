"""

"""

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def main():
    N = int(input())
    result = 0

    for i in range(1, N):
        result += len(make_divisors(i)) * len(make_divisors(N - i))

    print(result)


main()