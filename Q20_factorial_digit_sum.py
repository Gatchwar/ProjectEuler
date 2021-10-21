def main():
    from math import factorial
    # Get the factorial of 100 using factorial method in math, cast to string, split into its digits,
    # map digits to int and sum together
    print(sum(map(int, [digit for digit in str(factorial(100))])))


if __name__ == '__main__':
    main()
