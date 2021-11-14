from euler_module.euler_functions import prime_gen


# returns whether the integers passed in are permutations of each other by comparing their sorted strings
def is_permutation(first, second, third):
    return sorted(str(first)) == sorted(str(second)) == sorted(str(third))


def main():
    n = 10000
    bool_primes = prime_gen(n)
    primes = []
    # generate list of all 4 digit prime numbers
    for i in range(1000, 10000):
        if bool_primes[i]:
            primes.append(i)

    prime_length = len(primes)  # get length of list of 4 digit primes

    # iterate through the primes by index from the first to the third last
    for first in range(0, prime_length - 2):
        # iterate through the primes larger than the first by index to the second last
        for second in range(first + 1, prime_length - 1):
            # determine what would be the third number in an arithmetic series with the above two numbers
            third = (primes[second] - primes[first]) + primes[second]
            # if the three numbers form an arithmetic series
            if third in primes:
                # if they're also all permutations of each other and not the example sequence print and break
                if is_permutation(primes[first], primes[second], third) and primes[first] != 1487:
                    print('{}{}{}'.format(primes[first], primes[second], third))
                    break


if __name__ == '__main__':
    main()
