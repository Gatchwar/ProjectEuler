# returns a list of booleans of size n where each entry represents whether the number at that index is prime
def prime_gen(n):
    primes = [True for i in range(n + 1)]
    divisor = 2

    while divisor * divisor < n:
        if primes[divisor]:
            for i in range(divisor * divisor, n + 1, divisor):
                primes[i] = False
        divisor += 1

    # set 0 and 1 to False (not- prime) because they are not touched by the sieve above
    primes[0] = False
    primes[1] = False

    return primes


# returns a list of prime numbers up to n as integers as opposed to booleans
def prime_list(n):
    boolean_primes = prime_gen(n)
    actual_primes = []
    for i in range(n):
        if boolean_primes[i]:
            actual_primes.append(i)
    return actual_primes


# returns whether an integer n is prime by brute force checking until the square root
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Decorator. The underlying function must take only positional arguments, no keyword arguments.
class memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        else:
            val = self.func(*args)
            self.cache[args] = val
            return val
