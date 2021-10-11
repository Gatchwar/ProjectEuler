evens_list = []
first = 1
second = 2

while second < 4000000:
    if second % 2 == 0:
        evens_list.append(second)
    fib_sum = first + second
    first = second
    second = fib_sum

print(sum(evens_list))