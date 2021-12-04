from math import log10


def main():
    counter = 0
    # for each base between 1 and 9 (since 10 to any power has more digits than that power)
    for i in range(1, 10):
        digits = 1
        lg = log10(i)  # log i so as to not need to use exponentials
        while True:
            if lg * digits >= digits or lg * digits < digits - 1:
                break
            elif lg * digits > digits - 2:
                counter += 1
            digits += 1

    print(counter)


if __name__ == '__main__':
    main()
