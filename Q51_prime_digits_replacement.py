from euler_module.euler_functions import prime_gen

n = 1000000
primes = prime_gen(n)

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