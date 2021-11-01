from euler_module.euler_functions import prime_gen


def main():
    n = 2000000
    primes = prime_gen(n)

    summation = 0
    for i in range(2, 2000000):
        if primes[i]:
            summation += i

    print(summation)


if __name__ == '__main__':
    main()
