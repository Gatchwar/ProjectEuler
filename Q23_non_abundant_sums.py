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

    range_end = max(abundant) * 2 + 1  # largest number we expect to check is the largest abundant number generated doubled
    sums = [0 for _ in range(range_end)]  # a list of the sums that can be generated with the abundant numbers generated

    # for every combination of abundant numbers set sums value to 1 to indicate it can be the sum of 2 abundant numbers
    for first in abundant:
        for second in abundant:
            sums[first + second] = 1

    # for every number between 1 and 28123 (inclusive) check if it can be sum of abundant numbers if not add to total
    for summed_val in range(1, 28124):
        if sums[summed_val] == 0:
            total += summed_val

    print(total)


if __name__ == "__main__":
    main()
