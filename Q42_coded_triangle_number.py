# generator function that yields triangle numbers
def triangle_numbers():
    n = 1
    while True:
        n += 1
        yield n * (n + 1) // 2


# determine sum of values of letters in a word
def word_value(word):
    # for every letter in word call ord to get its unicode code point, subtract 96 so that a=1, b=2, ..., return the sum
    return sum([ord(letter)-64 for letter in word])


def main():
    triangle_counter = 0  # number of words with triangle number values
    triangle_list = [1]  # list of triangle numbers
    tri_gen = triangle_numbers()  # generator function that yields triangle numbers
    with open('external_files/Q42_words.txt', 'r') as f:
        # read in the file, remove the double quotes and make into a list by splitting on commas
        words = f.read().replace('\"', '').split(',')
        for word in words:
            value = word_value(word)
            # if the value of the current word is larger than the largest triangle number in the list
            if value > max(triangle_list):
                # while the largest triangle number in the list is less than the current value
                while max(triangle_list) < value:
                    # append triangle numbers to the list using the generator
                    triangle_list.append(next(tri_gen))
            # try to find the value in the list of triangle numbers
            if value in triangle_list:
                triangle_counter += 1

    f.close()
    print(triangle_counter)


if __name__ == '__main__':
    main()
