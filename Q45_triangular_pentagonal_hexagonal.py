# triangle number generator, yields the next triangular number
def triangle_numbers(n=1):
    while True:
        n += 1
        yield n * (n + 1) // 2


# pentagon number generator, yields the next pentagonal number
def pentagon_numbers(n=1):
    while True:
        n += 1
        yield n * (3 * n - 1) // 2


# hexagon number generator, yields the next hexagonal number
def hexagon_numbers(n=1):
    while True:
        n += 1
        yield n * (2 * n - 1)


def main():
    # instance current triangle and pentagon number
    triangle = 1
    pentagon = 1
    # instance generators for triangle, pentagon and hexagon numbers
    tri_gen = triangle_numbers()
    pent_gen = pentagon_numbers()
    hex_gen = hexagon_numbers()
    done = False  # stops the loop when the next number satisfying the condition is found
    while not done:
        # get the next hexagon number
        current = next(hex_gen)
        # while the current pentagon number is smaller than the current hexagon keep getting next pentagon number
        while current > pentagon:
            pentagon = next(pent_gen)
        # while the current pentagon number is smaller than the current hexagon keep getting next pentagon number
        while current > triangle:
            triangle = next(tri_gen)
        # if the current triangle, pentagon and hexagon number are the same and it isn't 40755 since we want next one
        if current == pentagon == triangle and current != 40755:
            print(current)  # print this number and end the loop
            done = True


if __name__ == '__main__':
    main()
