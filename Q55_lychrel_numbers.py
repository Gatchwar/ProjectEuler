# function that returns True if n is a Lychrel number (no palindrome sum in 49 iterations)
def is_lychrel(n):
    counter = 0
    # iterate 49 times to try to get a palindrome
    while counter < 50:
        n = n + int(str(n)[::-1])  # sum n with itself reversed
        # if n is a palindrome n is not a lychrel number so return False
        if str(n) == str(n)[::-1]:
            return False
        counter += 1
    return True


def main():
    # get the length of the list of the numbers less than 10000 for which is_lychrel return True
    print(len([i for i in range(10000) if is_lychrel(i)]))


if __name__ == '__main__':
    main()
