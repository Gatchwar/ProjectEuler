# generator function that yields triangle numbers
def pentagon_numbers(n=3):
    while True:
        n += 1
        yield n * (3 * n - 1) // 2


def main():
    penta_gen = pentagon_numbers()  # generator for pentagonal numbers
    pentagons = [1, 5, 12]  # instance a list with the first 3 pentagonal numbers to begin
    j = 1  # index of the smaller pentagon number
    k = 2  # index of larger pentagon number
    while True:
        add = pentagons[j] + pentagons[k]
        diff = pentagons[k] - pentagons[j]
        # if the sum of the pentagonal numbers is larger than the largest known pentagon number
        if add > pentagons[-1]:
            # use the generator to add pentagon numbers until the largest is at least as large as the sum
            while add > pentagons[-1]:
                pentagons.append(next(penta_gen))
        if add in pentagons and diff in pentagons:
            # print('pentagonJ: {} pentagonK: {}'.format(pentagons[j], pentagons[k])) # print pentagon numbers j and k
            print(diff)
            break  # break because given the way the space is being searched the first valid pair is also the smallest
        j += 1  # increment the smaller index
        if j == k:  # if the smaller index has caught up to the larger index
            j = 1  # reset the smaller index to 1 and begin counting towards the larger index again
            k += 1  # increment the larger index


if __name__ == '__main__':
    main()
