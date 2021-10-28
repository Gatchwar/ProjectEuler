def count(arr, coin, total):
    # If total < 0 or if total > 0 but no coins there is no way to make change
    if total < 0 or (coin <= 0 and total >= 1):
        return 0

    # If total is 0 there is only 1 way to make change
    if total == 0:
        return 1

    # count is sum of solutions including a given coin and those without it
    return count(arr, coin - 1, total) + count(arr, coin, total - arr[coin - 1])


def main():
    denominations = [1, 2, 5, 10, 20, 50, 100, 200]
    num_denoms = len(denominations)
    amount = 200

    print(count(denominations, num_denoms, amount))


if __name__ == '__main__':
    main()
