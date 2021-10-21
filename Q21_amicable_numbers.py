from functools import reduce


def factor_sum(n):
    # for ints between 1 and sqrt n (inclusive), if i divides n then make a list with i and n//i, reduce the lists using
    # the add function of lists, make a set with those numbers, get the sum, subtract n to get sum of all factors < n
    return sum(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))-n


def main():
    amicable = 0
    factor_sums = {1: 1}  # set 1 to have value 1 in order to avoid key errors due to prime numbers
    for i in range(2, 10000):  # skip 1 since 1 has 0 factors smaller than itself
        factor_sums[i] = factor_sum(i)

    for key in factor_sums:
        a = factor_sums[key]
        if a >= 10000:  # some keys have a value greater than 10000 which has no dict entry, skip those
            continue
        else:
            if key == factor_sums[a]:  # if d(a) = key and d(key) = a
                if key != a:  # a cannot equal b
                    amicable += key

    print(amicable)


if __name__ == '__main__':
    main()
