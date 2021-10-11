biggest_pal = 0

for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        prod = x * y
        if str(prod) == str(prod)[::-1]:
            if prod > biggest_pal:
                biggest_pal = prod

print(biggest_pal)
