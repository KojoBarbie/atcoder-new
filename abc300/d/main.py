import math

def sieve(n):
    primes = []
    for i in range(2, n+1):
        is_prime = True
        for p in primes:
            if p * p > i:
                break
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

def count_primes():
    n = int(input())
    primes = sieve(int(n ** 0.5) + 1)
    count = 0
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            for k in range(j+1, len(primes)):
                if primes[i]**2 * primes[j] * primes[k]**2 <= n:
                    count += 1
                else:
                    break
    print(count)

count_primes()