n = 2000000
primes = [True for i in range(n+1)]
divisor = 2

while divisor * divisor < n:
    if primes[divisor]:
        for i in range(divisor * divisor, n+1, divisor):
            primes[i] = False
    divisor += 1

summation = 0
for i in range(2, 2000000):
    if primes[i]:
        summation+=i

print(summation)