from euler_module.euler_functions import prime_gen

n = 1000000
primes = prime_gen(n)

digs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

seen = set()
consecutive = 8


def thing(a, digits):
    for i in range(digits - 2):
        for j in range(i + 1, digits - 1):
            str_num = [dig for dig in str(a)]
            str_num[i] = str_num[j] = '*'
            if ''.join(str_num) not in seen:
                counter = 0
                for val in digs:
                    str_num[i] = str_num[j] = val
                    if primes[int(''.join(str_num))]:
                        counter += 1
                        str_num[i] = str_num[j] = '*'
                        print(''.join(str_num))
                if counter >= consecutive:
                    print(a)
                str_num[i] = '*'
                str_num[j] = '*'
                seen.add(''.join(str_num))


def main():
    digits = 3
    while True:
        low = 10 ** (digits-1)
        high = 10 ** digits
        for num in range(low, high):
            if primes[num]:
                thing(num, digits)
        digits += 1


if __name__ == '__main__':
    main()
