factors = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

num = 20

while True:
    is_multiple = True
    for factor in factors:
        if num % factor != 0:
            is_multiple = False
            break
    if is_multiple:
        print(num)
        break
    num += 20