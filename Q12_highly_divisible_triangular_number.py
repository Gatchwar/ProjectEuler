from functools import reduce


# for all integers x between 1 and sqrt(n) if x is a factor of n add it and its paired factor n/x to a list which gets reduced to a set and we check how big it is
def num_factors(n):
    return len(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))


triangle = 0
natural = 1
threshold = 500
while True:
    triangle += natural
    natural += 1
    if num_factors(triangle) >= threshold:
        print(triangle)
        break
