def divisors(param_number: int):
    temp = param_number
    divisor = 2
    while True:
        if param_number % divisor == 0:
            print(f"{param_number:<{len(str(temp))}}  | {divisor}")
            param_number = int(param_number / divisor)
        else:
            if divisor == (int(temp ** .5) + 1):
                print(f"{param_number:<{len(str(temp))}}  | {param_number}")
                break
            elif param_number == 1:
                print(f"{param_number:<{len(str(temp))}}  | {param_number}")
                break
            divisor += 1

divisors(600851475143)