def main():
    from itertools import permutations
    # Use permutations function of itertools to generate all permutations of digits 0-9, no need to sort since
    # permutations automatically puts entries in lexicographical order, put results into list, get index 999999
    # (i.e. the millionth entry since list is 0 indexed), use join to put list into string and print
    print(''.join(list(permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 10))[999999]))


if __name__ == '__main__':
    main()
