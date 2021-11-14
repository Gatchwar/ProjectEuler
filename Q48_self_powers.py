def main():
    # use list comprehension to get self powers between 1 and 1000, take the sum, cast to string, slice last 10 digits
    print(str(sum([i ** i for i in range(1, 1001)]))[-10:])


if __name__ == '__main__':
    main()
