def main():
    curious = 0
    # implement a dictionary for the factorials of the single digit numbers
    factorials = {'0': 1, '1': 1, '2': 2, '3': 6, '4': 24, '5': 120, '6': 720, '7': 500, '8': 40320, '9': 362880}
    # do not check 1 or 2 because those are specifically not to be counted, set 100'000'000 as upper limit
    for num in range(3, 100000000):
        total = 0
        for digit in str(num):
            total += factorials[digit]
        # if the sum of the factorials of the digits equals the number add it to the total
        if total == num:
            curious += num

    print(curious)


if __name__ == '__main__':
    main()
