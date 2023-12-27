from math import sqrt

def generate_primes_up_to(n):
    sieve = {number: True for number in range(2, n + 1)}

    for number in range(2, int(sqrt(n))):
        if sieve[number]:
            for multiple in range(number ** 2, n + 1, number):
                sieve[multiple] = False

    primes = [number for number, is_prime in sieve.items() if is_prime]
    return primes, sieve

PRIMES, SIEVE = generate_primes_up_to(2_001_000)

t = int(input())

for _ in range(t):
    n = int(input()) * 2

    for a in PRIMES:
        if SIEVE[n - a]:
            print(a, n - a)
            break
