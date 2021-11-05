from euler_module.euler_functions import is_prime
from itertools import permutations


def main():
    largest = 0
    # use done flag to know when the first pandigital prime is found, no need to search numbers with fewer digits
    done = False
    for n in range(10, 0, -1):
        # when first pandigital prime is found, the done flag is raised and the iteration for fewer digits is not done
        if done:
            break
        # generate list of permutations of numbers in range 1 - (n-1)
        pandigitals = list(permutations(range(1, n)))
        for perm in pandigitals:
            # no prime number ends with these digits
            if perm[-1] not in {2, 4, 5, 6, 8}:
                i = int(''.join(map(str, perm)))
                if is_prime(i):
                    done = True
                    if i > largest:
                        largest = i

    print(largest)


if __name__ == '__main__':
    main()
