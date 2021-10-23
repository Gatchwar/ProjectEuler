def main():
    second = 1
    add = 1  # the sum of the previous 2 fibonacci numbers begin at 1 which is the sum of 0 and 1
    index = 2  # index of current fibonacci number, start at 2 because 1 is second fibonacci number [1, 1, ...]
    # iterate while the length of the currently indexed fibonacci number is less than 1000
    while len(str(add)) < 1000:
        first = second
        second = add
        index += 1
        add = first + second

    print(index)
    # print(add)  # prints out the first 1000 digit fibonacci number if curious


if __name__ == '__main__':
    main()
