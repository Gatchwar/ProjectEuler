# build a dictionary of numbers with known collatz sequence lengths add in 1 as the base case
num_dict = {1: 1}


def collatz(n):
    terms = 1
    current = n
    while True:
        if current % 2 == 0:
            current //= 2
        else:
            current = 3 * current + 1
        # if current number already in dictionary
        if current in num_dict:
            # the dictionary entry for input n is the current terms + the terms of the existing entry
            num_dict[n] = terms + num_dict[current]
            return
        terms += 1


def main():
    # for all integers between 2 (1 is already in the dict) and 1'000'000
    for i in range(2, 1000000):
        collatz(i)

    print("Number: " + str(max(num_dict, key=num_dict.get)))
    print("Collatz sequence length: " + str(max(num_dict.values())))


if __name__ == "__main__":
    main()
