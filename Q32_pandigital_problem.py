from itertools import permutations


def main():
    # instance a set to store the pandigital products
    products = set()
    # get list of all permutations of the 9 digits 1-9
    arrangements = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9']))
    # for each of the permutations of the 9 digits
    for iteration in arrangements:
        # select a spot to insert the multiplication sign
        # none of the pandigital equations can have a 3 digit product or smaller
        for multiply in range(1, 6):
            # select a spot after the multiplication sign to put the equals sign
            for equals in range(multiply+1, 7):
                # make the product by joining the relevant slices of the array
                prod = int(''.join(iteration[equals:]))
                # if pandigital equation
                if int(''.join(iteration[:multiply])) * int(''.join(iteration[multiply:equals])) == prod:
                    products.add(prod)

    print(sum(products))


if __name__ == '__main__':
    main()
