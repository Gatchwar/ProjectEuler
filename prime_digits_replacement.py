n = 1000000
primes = [True for i in range(n+1)]
divisor = 2

while divisor * divisor < n:
    if primes[divisor]:
        for i in range(divisor * divisor, n+1, divisor):
            primes[i] = False
    divisor += 1

print("finished generating primes")

digits = 6


def build(ind1, ind2, dig1, dig2, dig3, dig4):
    arr = ['x', 'x', 'x', 'x', 'x', 'x']
    arr[ind1] = '*'
    arr[ind2] = '*'
    for i in range(digits):
        if arr[i] == 'x':
            arr[i] = dig1
            break
    for i in range(1, digits):
        if arr[i] == 'x':
            arr[i] = dig2
            break
    for i in range(2, digits):
        if arr[i] == 'x':
            arr[i] = dig3
            break
    for i in range(3, digits):
        if arr[i] == 'x':
            arr[i] = dig4
            break
    return arr


def thing(arr, ind1, ind2):
    counter = 0
    found = False
    for i in range(10):
        arr[ind1] = str(i)
        arr[ind2] = str(i)
        val = int(''.join(arr))
        if primes[val]:
            if not found:
                smallest = val
                found = True
            counter += 1

    if counter == 7:
        print(smallest)


def generate_primes():
    for j in range(0, digits - 1):
        for k in range(j+1, digits):
            for l in range(10):
                for m in range(10):
                    for o in range(10):
                        for p in range(10):
                            temp = build(j, k, str(l), str(m), str(o), str(p))
                            thing(temp, j, k)

# print(build(1, 3, '1', '2', '3'))
# thing(['1', '2', '1', '3', '1', '3'], 0, 2)
# primes_list = generate_primes(10000000)

print(primes[121312])

# generate_primes()

#
# Solution to Project Euler problem 51
# Copyright (c) Project Nayuki. All rights reserved.
#
# https://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
#


# def compute():
#     isprime = primes
#     for i in range(len(isprime)):
#         if not isprime[i]:
#             continue
#
#         n = [int(c) for c in str(i)]
#         for mask in range(1 << len(n)):
#             digits = do_mask(n, mask)
#             count = 0
#             for j in range(10):
#                 if digits[0] != 0 and isprime[to_number(digits)]:
#                     count += 1
#                 digits = add_mask(digits, mask)
#
#             if count == 8:
#                 digits = do_mask(n, mask)
#                 for j in range(10):
#                     if digits[0] != 0 and isprime[to_number(digits)]:
#                         return str(to_number(digits))
#                     digits = add_mask(digits, mask)
#     raise AssertionError("Not found")
#
#
# def do_mask(digits, mask):
#     return [d * ((~mask >> i) & 1) for (i, d) in enumerate(digits)]
#
#
# def add_mask(digits, mask):
#     return [d + ((mask >> i) & 1) for (i, d) in enumerate(digits)]
#
#
# def to_number(digits):
#     result = 0
#     for d in digits:
#         result = result * 10 + d
#     return result
#
#
# if __name__ == "__main__":
#     print(compute())