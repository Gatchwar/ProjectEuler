
def main():
    # generate list of the product a^b for a in range 2-101 and for b in range 2-101, cast to set to remove duplicates
    # call len() to get the amount of numbers in the set
    print(len(set([a ** b for b in range(2, 101) for a in range(2, 101)])))


if __name__ == '__main__':
    main()
