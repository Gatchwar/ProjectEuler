from euler_module.euler_functions import is_prime
from itertools import permutations

factors = [2, 3, 5, 7, 11, 13, 17]


# returns the pandigital as an integer if it satisfies the condition and 0 otherwise
def substring_divis(s):
    # for each substring divisor
    for sub in range(7):
        # check if that slice of s is divisible by the corresponding prime, if not return 0
        if int(s[1 + sub: 4 + sub]) % factors[sub] != 0:
            return 0
    return int(s)


def main():
    total = 0
    # generate a lit of the permutations of the digits 0-9
    pandigitals = list(permutations(range(10)))
    for perm in pandigitals:
        total += substring_divis(''.join(map(str, perm)))

    print(total)


if __name__ == '__main__':
    main()
