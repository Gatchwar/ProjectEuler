from euler_module.euler_functions import is_prime


def main():
    n = 170000000
    # primes = prime_gen(n)

    done = False
    skip = 2  # how many numbers ahead is the next diagonal
    prime_counter = 0
    diagonal_counter = 1
    current = 1  # current number in the spiral
    side_length = 1
    while not done:
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
