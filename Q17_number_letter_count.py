def main():
    number_dict = {
        0: 0,  # zero in the case there's a zero in the tens column of a number between 100-1000
        1: 3,
        2: 3,
        3: 5,
        4: 4,
        5: 4,
        6: 3,
        7: 5,
        8: 5,
        9: 4,
        10: 3,
        11: 6,
        12: 6,
        13: 8,
        14: 8,
        15: 7,
        16: 7,
        17: 9,
        18: 9,
        19: 8,
        20: 6,
        30: 6,
        40: 5,
        50: 5,
        60: 5,
        70: 7,
        80: 6,
        90: 6,
        100: 10,
        200: 10,
        300: 12,
        400: 11,
        500: 11,
        600: 10,
        700: 12,
        800: 12,
        900: 11,
    }
    letters = 0
    for ones in range(1, 10):
        letters += number_dict[ones]
    for tens in range(10, 100):
        if tens in number_dict:
            letters += number_dict[tens]
        else:
            letters += number_dict[int(str(tens)[0] + '0')]
            letters += number_dict[int(str(tens)[1])]
    for hundreds in range(100, 1000):
        if hundreds in number_dict:
            letters += number_dict[hundreds]
        else:
            letters += number_dict[int(str(hundreds)[0] + '00')]
            letters += 3  # the 'and' in x hundred AND x
            letters += number_dict[int(str(hundreds)[1] + '0')]
            letters += number_dict[int(str(hundreds)[2])]
    letters += 11  # one thousand
    print(letters)


if __name__ == "__main__":
    main()
