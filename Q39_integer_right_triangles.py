def main():
    most_solutions = 0
    best_p = 12
    # iterate from 12 (the smallest perimeter made up of integer side lengths (3, 4, 5)) and 1000
    for p in range(120, 1000 + 1):
        solutions = 0
        for a in range(1, p//2):
            for b in range(a + 1, p // 2):
                c = p - a - b
                if a ** 2 + b ** 2 == c ** 2:
                    solutions += 1
        if solutions > most_solutions:
            best_p = p
            most_solutions = solutions

    print(best_p)


if __name__ == '__main__':
    main()
