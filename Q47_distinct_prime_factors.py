from euler_module.euler_functions import prime_gen

# generate a list of all prime numbers less than n
n = 1000000
bool_primes = prime_gen(n)
primes = []
for number in range(2, n):
    if bool_primes[number]:
        primes.append(number)


# returns the number of unique factors possessed by a number
def prime_factorization(n):
    factors = set()  # use a set for the factors since we need unique factors
    prime_index = 0  # index of potential prime factor
    # when n is reduced to 1 the n has been fully factorized
    while n != 1:
        # repeatedly divide n by the current prime factor
        while n % primes[prime_index] == 0:
            factors.add(primes[prime_index])
            n /= primes[prime_index]
        prime_index += 1

    return len(factors)  # return length of set which denotes unique prime factors


def main():
    consecutive = 4  # how many consecutive numbers need to be found
    num_factors = 4  # how many factors in each number
    counter = 0  # how many consecutive numbers with the requisite number of factors currently
    i = 647  # starting index
    # while True with a break when value found since unknown how large the needed number is
    while True:
        # check if number is prime since have 1 factor by definition (besides 1) and will take long time to factor
        # and check if the number of unique factors is the number needed
        if i not in primes and prime_factorization(i) >= num_factors:
            counter += 1
            if counter == consecutive:
                print(i - consecutive + 1)
                break
        else:
            counter = 0

        i += 1


if __name__ == '__main__':
    main()
