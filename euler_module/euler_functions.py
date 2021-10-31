def prime_gen(n):
    primes = [True for i in range(n + 1)]
    divisor = 2

    while divisor * divisor < n:
        if primes[divisor]:
            for i in range(divisor * divisor, n + 1, divisor):
                primes[i] = False
        divisor += 1

    primes[0] = False
    primes[1] = False

    return primes


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
