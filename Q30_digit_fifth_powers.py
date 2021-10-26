def main():
    # instance a list to store the numbers that meet the digit fifth power criteria
    digit_fifth_powers = []
    # try every number starting at 2 (since 1 doesn't count) and end at a decently big number
    for number in range(2, 10000000):
        fifth_power = sum([int(digit) ** 5 for digit in str(number)])
        if fifth_power == number:
            digit_fifth_powers.append(fifth_power)

    print(sum(digit_fifth_powers))
    # print(digit_fifth_powers)  # print out the digit fifth power numbers if curious


if __name__ == '__main__':
    main()
