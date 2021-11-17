from euler_module.euler_functions import prime_list


def main():
    n = 1000000
    longest = 0

    primes = prime_list(n)
    most_terms = 0
    for i in range(len(primes)):
        total = primes[i]
        terms = 1
        for j in range(i + 1, len(primes)):
            total += primes[j]
            terms += 1
            if total >= n:
                break
            if total in primes and terms > most_terms:
                longest = total
                most_terms = terms
    print(longest)


if __name__ == '__main__':
    main()
