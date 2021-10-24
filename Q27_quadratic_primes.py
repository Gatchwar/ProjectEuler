# list of all primes up to 1000 generated using a Sieve of Eratosthenes, hardcoded to save compute time
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
          103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
          223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337,
          347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
          463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
          607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
          743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881,
          883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


# returns true if n is prime and false otherwise
def is_prime(n):
    # the primes up to 1000 are known, leverage them
    if n < 1000:
        return True if n in primes else False
    # for larger numbers (n >= 1000) check every number between 2 and sqrt(n) for factors, if any are, it isn't prime
    elif n >= 1000:
        for factor in range(2, int(n ** 0.5) + 1):
            if n % factor == 0:
                return False
        return True


def main():
    max_primes = 0  # tracks the n value with the most known consecutive primes using the formula
    max_a = 0
    max_b = 0
    # |a| < 1000 which means -999 - 999 are valid
    for a in range(-999, 1000):
        # b must be prime so that the n = 0 case works, no considerations for b < 0 because primes must be positive
        for b in primes:
            n = 0
            # use done flag to know when to end the loop
            done = False
            # while n^2 + an + b is prime keep incrementing n, when n isn't prime end loop
            while not done:
                if is_prime(n**2 + a * n + b):
                    n += 1
                else:
                    done = True
            # if n > the current longest consecutive chain of primes replace max_primes and set the a and b values
            if n > max_primes:
                max_primes = n
                max_a = a
                max_b = b

    print(max_a * max_b)
    # print("a: {}, b: {}, n: {}".format(max_a, max_b, max_primes))  # print a, b and n values of the largest n value


if __name__ == '__main__':
    main()
