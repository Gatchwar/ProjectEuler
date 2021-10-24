def longest_recurring_cycle(denominator):
    cycle = ''  # instance an empty string to hold the digits after the decimal
    remainders = {}  # instance a dict to store the known remainders as keys and their positions as values
    rem = 1 % denominator  # get first remainder
    # while the remainder is not 0 (which means there is no recurring cycle)
    # and it isn't in the dict (meaning a recurring cycle was found)
    while (rem != 0) and (rem not in remainders):
        remainders[rem] = len(cycle)  # add entry to dict for current iteration
        rem *= 10
        cycle += str(rem // denominator)
        rem %= denominator
    # if the remainder ever reaches 0 there is no infinitely repeating cycle
    if rem == 0:
        return 0
    # else return the length of the cycle string that repeats
    else:
        return len(cycle[remainders[rem]:])


def main():
    d = -1  # the denominator value with the longest recurring cycle
    longest_cycle = 0  # the length of the currently known longest recurring cycle
    # iterate over the numbers 1 - 999 (do not start at 0 because 1/0 is undefined)
    for denominator in range(1, 1000):
        cycle_length = longest_recurring_cycle(denominator)
        # if the longest cycle in the current denominator value is greater or equal to the current longest replace it
        if cycle_length >= longest_cycle:
            d = denominator
            longest_cycle = cycle_length

    print(d)
    # print(longest_cycle)  # prints out the length of the longest cycle if you're curious


if __name__ == '__main__':
    main()
