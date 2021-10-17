from math import comb


def main():
    length = 20
    width = 20
    # paths are based on the number of horizontal and vertical segments
    # that must be traversed len+width choose length or width used width
    print(comb(length + width, width))


if __name__ == '__main__':
    main()
