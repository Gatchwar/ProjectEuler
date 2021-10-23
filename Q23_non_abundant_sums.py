from functools import reduce


# for ints between 1 and sqrt n (inclusive), if i divides n then make a list with i and n//i, reduce the lists using
# the add function of lists, make a set with those numbers, get the sum, subtract n to get sum of all factors < n
def factor_sum(n):
    return sum(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))-n


def main():
    total = 0
    abundant = []
    # 28123 is the largest number that cannot summed from 2 abundant numbers, 28124 is the first number that must be,
    # 12 is the smallest abundant number
    for i in range(12, 28124):
        if factor_sum(i) > i:
            abundant.append(i)

    # instance a set of all numbers that are a sum of abundant numbers
    sums = set()
    length = len(abundant)
    # for every combination of numbers
    for first in range(length):
        for second in range(first, length):
            sums.add(abundant[first] + abundant[second])

    # for every number between 1 and 28123 (inclusive) check if it can be sum of abundant numbers if not add to total
    for summed_val in range(1, 28124):
        if summed_val not in sums:
            total += summed_val

    print(total)


if __name__ == "__main__":
    main()
