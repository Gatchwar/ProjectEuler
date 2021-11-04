def main():
    from math import prod
    # experimentally the millionth digit falls around 185'000, make string of numbers from 0-199'999
    d = ''.join([str(i) for i in range(200000)])
    # indices of digits to get
    indices = [1, 10, 100, 1000, 10000, 100000, 1000000]
    # print the product of the digits in the string d at the indices specified
    print(prod([int(d[j]) for j in indices]))

    # single line implementation using list comprehensions, very hard to parse so submitted the 3 line version
    # print(prod([int(''.join([str(i) for i in range(200000)])[j]) for j in [1,10,100,1000,10000,100000,1000000]]))


if __name__ == '__main__':
    main()
