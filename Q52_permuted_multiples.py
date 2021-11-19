# function that returns the input cast to a string then sorted
def perm(x):
    return sorted(str(x))


def main():
    n = 1
    # loop infinitely and use break to end loop
    while True:
        # check if n, 2n, 3n, 4n, 5n, and 6n when cast to strings and sorted are the same (i.e. permutations)
        if perm(n) == perm(n * 2) == perm(n * 3) == perm(n * 4) == perm(n * 5) == perm(n * 6):
            print(n)
            break
        n += 1


if __name__ == '__main__':
    main()
