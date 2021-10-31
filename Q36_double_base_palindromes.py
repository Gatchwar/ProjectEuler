def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


def main():
    # for every number up to 999'999 cast number to string and check if it is a palindrome, also cast to binary,
    # remove the 0b prefix and check if that is a palindrome, if both pass add to list and take sum at the end
    print(sum([i for i in range(1000000) if is_palindrome(str(i)) and is_palindrome(bin(i).replace('0b', ''))]))


if __name__ == '__main__':
    main()
