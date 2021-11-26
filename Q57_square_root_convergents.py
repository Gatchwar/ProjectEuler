from fractions import Fraction
from itertools import islice
from math import log10


# get log of the numerator and denominator, cast to int to truncate decimals, return True if numerator > denominator
def longer(frac):
    return True if int(log10(frac.numerator)) > int(log10(frac.denominator)) else False


# return a Fraction of the continued fraction approximation of sqrt2
def cont_fraction(a, b, iterations):
    terms = list(islice(zip(a, b), iterations))
    z = Fraction(2, 1)
    for a, b in reversed(terms):
        z = a + b / z
    return z


def main():
    larger = 0
    a = [1] + [2 for _ in range(999)]
    b = [1 for _ in range(1000)]
    for i in range(1000):
        if longer(cont_fraction(a[:i], b[:i], i)):
            larger += 1
    print(larger)


if __name__ == '__main__':
    main()
