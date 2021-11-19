from math import comb


def main():
    counter = 0
    for n in range(1, 101):
        for r in range(1, n):
            if comb(n, r) > 1000000:
                counter += 1
    print(counter)


if __name__ == '__main__':
    main()
