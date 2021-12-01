# function that yields cubic numbers starting from the argument n which defaults to 1
def cube_gen(n=1):
    while True:
        yield n ** 3
        n += 1


def main():
    done = False  # boolean to determine when to end the main while loop since unknown how far to search
    digits = 1  # since permutations must have the same number of digits use this to know when to restart the dict
    cubes = cube_gen()  # instantiate the cubic number generator
    cube = next(cubes)  # get the first cubic number
    while not done:
        temp = dict()  # instance temporary array to track numbers and permutations with this many digits
        # for all numbers with digits digits try to find permutations, reset the dict when digits increases
        while len(str(cube)) == digits:
            cube_str = ''.join(sorted(str(cube)))  # sort the digits of the cube, permutations will share this string
            # if yet to see this string of numbers with this many digits then this is the lowest number with this string
            if cube_str not in temp:
                temp[cube_str] = [cube, 1]  # create entry in dict with cube string as key, the number and a counter
            # if this string of numbers has been seen already then this is a permutation of a previous number
            else:
                temp[cube_str][1] += 1  # increment the counter for this string
                # if this string's counter is 5 then this string has 5 cubic permutations
                if temp[cube_str][1] == 5:
                    print(temp[cube_str][0])  # print the lowest number with this string
                    done = True  # set the done flag to end the large while loop
                    break  # break to end the current while loop
            cube = next(cubes)
        digits += 1


if __name__ == '__main__':
    main()
