def main():
    largest = 0
    # check numbers between 1 - 9999, since n must be at least 2 then 5+ digit numbers are at least 10 digits
    for i in range(1, 10000):
        pandigital_string = str(i)  # begin the pandigital string with i * 1
        n = 2  # start the multiplier at n = 2 since n = 1 is accounted for above
        # while the length of the string is less than 9 append i * n where n = 2, 3, 4, ... to build pandigital string
        while len(pandigital_string) < 9:
            pandigital_string += str(i * n)
            n += 1

        # if the length of the string is greater than 9 it's too long to be pandigital
        if len(pandigital_string) == 9:
            # if the string is exactly 9 numbers long but has any 0s it isn't pandigital since 0 isn't allowed
            if '0' not in pandigital_string:
                # if a set formed out of the string isn't of length 9 (i.e. there are duplicates) it isn't pandigital
                if len(set(pandigital_string)) == 9:
                    pandigital_num = int(pandigital_string)
                    # if the current pandigital number is greater than the largest seen thus far replace the largest
                    if pandigital_num > largest:
                        largest = pandigital_num

    print(largest)


if __name__ == '__main__':
    main()
