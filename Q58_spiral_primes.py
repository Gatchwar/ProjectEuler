from euler_module.euler_functions import is_prime


def main():
    done = False
    skip = 2  # how many numbers ahead is the next diagonal
    prime_counter = 0
    diagonal_counter = 1
    current = 1  # current number in the spiral
    side_length = 1
    # use done boolean to end loop since it is not known how many iterations this will take
    while not done:
        # for every corner in the current layer
        for corner in range(4):
            current += skip
            if is_prime(current):
                prime_counter += 1
            diagonal_counter += 1
        side_length += 2
        if prime_counter / diagonal_counter < 0.1:
            print(side_length)
            done = True
        skip += 2


if __name__ == '__main__':
    main()
