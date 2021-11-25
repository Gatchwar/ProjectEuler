def main():
    largest = 0
    for a in range(1, 100):
        for b in range(1, 100):
            # get digit sum by performing a ** b, cast to string, use list comprehension to split then sum the digits
            digit_sum = sum([int(i) for i in str(a ** b)])
            if digit_sum > largest:
                largest = digit_sum

    print(largest)


if __name__ == '__main__':
    main()
