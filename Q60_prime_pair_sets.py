from euler_module.euler_functions import prime_gen, is_prime
from itertools import combinations
import functools

n = 100000000
prime_bools = prime_gen(n)
primes = [str(i) for i in range(n) if prime_bools[i]]


# decorate this function with infinite size cache because it will be called with the same values often
@functools.lru_cache(maxsize=None)
def is_cat_prime(x, y):
    cat_num = int(x + y)
    if cat_num < n:
        return prime_bools[cat_num]
    else:
        return is_prime(cat_num)


# given a list of 5 indices return True if all combinations are prime False otherwise
def prime_pairs(indices):
    combs = combinations(indices, 2)
    for pair in combs:
        if not is_cat_prime(primes[pair[0]], primes[pair[1]]):
            return False
        if not is_cat_prime(primes[pair[1]], primes[pair[0]]):
            return False
    return True


def main():
    done = False

    i1 = 0
    i2 = 1
    i3 = 2
    i4 = 3
    i5 = 4
    while not done:
        if prime_pairs([i1, i2, i3, i4, i5]):
            print(sum([primes[i1], primes[i2], primes[i3], primes[i4], primes[i5]]))
            done = True  # break after the first thing found because it is guaranteed to be the smallest

        if i4 + 1 == i5:
            if i3 + 1 == i4:
                if i2 + 1 == i3:
                    if i1 + 1 == i2:
                        i1 = 0
                        i2 = 1
                        i3 = 2
                        i4 = 3
                        i5 += 1
                        print(i5)
                    else:
                        i1 += 1
                else:
                    i2 += 1
            else:
                i3 += 1
        else:
            i4 += 1


if __name__ == '__main__':
    main()
