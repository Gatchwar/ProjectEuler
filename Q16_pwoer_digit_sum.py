def main():
    # get 2^1000 as a string, split the digits apart and map them to integers, sum those together
    print(sum(map(int, [number for number in str(2**1000)])))


if __name__ == "__main__":
    main()
