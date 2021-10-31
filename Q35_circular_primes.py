# return True if n is prime else False
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# returns True if all rotation of input n are prime and False otherwise
def are_rotations_prime(n):
    str_n = str(n)
    list_n = list(str_n)
    # iterate 1 fewer than the length of n times since n is already known to be prime
    for _ in range(len(str_n)-1):
        # pop the front element and append it to the end
        list_n.append(list_n.pop(0))
        # if current rotation isn't prime return False
        if not is_prime(int(''.join(list_n))):
            return False
    return True


def main():
    # hard code primes up to 100 because they're literally in the question
    circular_primes = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]

    # check every number between 100 (since we were given the primes < 100) and 999'999
    for num in range(100, 1000000):
        if is_prime(num):
            if are_rotations_prime(num):
                circular_primes.append(num)

    print(len(circular_primes))
    # print(circular_primes)  # print the circular primes if curious


if __name__ == '__main__':
    main()
