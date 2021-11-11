from euler_module.euler_functions import prime_gen


# given a composite number determines if Golbach's other conjecture holds returns True if yes and False otherwise
def composite_check(primes, num):
    prime_index = 0
    while primes[prime_index] + 2 <= num:
        square = (num - primes[prime_index])
        if is_golbach(square):
            return True
        prime_index += 1
    return False


# given a number n determine if n can be made up of 2 * (i^2) where i is an integer
def is_golbach(n):
    i = 1
    while (i ** 2) * 2 <= n:
        if (i ** 2) * 2 == n:
            return True
        i += 1
    return False


def main():
    # quicker to generate a large number of primes at once using sieve of Eratosthenes, increase n if needed
    n = 10000
    numbers = prime_gen(n)
    primes = []
    composites = []
    # each boolean in the generated array is True if prime and False if composite
    for number in range(2, n):
        # if the number at index number is prime append it to the primes list
        if numbers[number]:
            primes.append(number)
        # if the number at index number is composite
        else:
            # if the number is also odd append to composites list to be checked
            if number % 2 == 1:
                composites.append(number)

    # for each odd composite check if Golbach's other conjecture holds if not prime and break since we only need one
    for c in composites:
        if not composite_check(primes, c):
            print(c)
            break


if __name__ == '__main__':
    main()
