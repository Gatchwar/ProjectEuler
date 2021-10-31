from euler_module.euler_functions import prime_gen

n = 1000000  # how many numbers are evaluated for primality
primes = prime_gen(n)  # use imported function to get lookup table for primes up to 1'000'000


# returns True if the every truncation of the number is prime and False otherwise
def is_truncatable(number):
    str_num = str(number)
    truncations = len(str_num)  # determine how many truncations in either direction are needed
    # truncate the leftmost digits
    for left_truncate in range(1, truncations):
        # if the truncated number isn't in the lookup table it isn't prime
        if not primes[int(str_num[left_truncate:])]:
            return False
    # truncate the rightmost digits
    for right_truncate in range(1, truncations):
        # if the truncated number isn't in the lookup table it isn't prime
        if not primes[int(str_num[:-right_truncate])]:
            return False
    # all truncations are prime return True
    return True


def main():
    truncatable_primes = 0
    found = 0  # count how many truncatable primes have been found
    i = 10  # start from 10 since none of the single digit primes count
    # loop until 11 truncatable primes are found or we exhaust the lookup table
    while found < 11 and i < n:
        # check if i is prime and leverage lazy evaluation to only check if its truncatable afterwards
        if primes[i] and is_truncatable(i):
            truncatable_primes += i
            found += 1
        i += 1

    print(truncatable_primes)


if __name__ == '__main__':
    main()
