def main():
    total = 1  # sum of diagonals, start with the 1 in the center accounted for
    counter = 1  # current corner value, start the counter at 1
    skip = 2  # how many numbers ahead is the next diagonal

    while skip < 1001:
        # for each corner in that layer, increment the counter, add the counter to the total
        for corner in range(4):
            counter += skip
            total += counter
        # move to the next layer where the corners are 2 numbers further apart than before
        skip += 2

    print(total)


if __name__ == "__main__":
    main()
