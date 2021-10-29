from fractions import Fraction


def main():
    final_numerator = 1
    final_denominator = 1
    # 10 is the first 2 digit number and 98 will be the last meaningful check since 99 over anything will be at least 1
    for numerator in range(10, 99):
        # denominator needs to be bigger than numerator for fraction < 1.0 and caps at the last 2 digit number 99
        for denominator in range(numerator + 1, 100):
            # cast the numerator and denominator to string in order to slice it
            num_str = str(numerator)
            den_str = str(denominator)
            # for each digit in the numerator
            for num_digit in range(2):
                # for each digit in the denominator
                for den_digit in range(2):
                    # if the values of the currently selected digits match
                    if num_str[num_digit] == den_str[den_digit]:
                        # if that matching digit isn't 0
                        if num_str[num_digit] != '0':
                            # slice the non-matching digit out
                            re_num = int(num_str[(num_digit + 1) % 2])
                            re_den = int(den_str[(den_digit + 1) % 2])
                            # if the denominator digit isn't 0 because that leads to undefined behaviour
                            if re_den != 0:
                                # if the curious fraction is equivalent to the original fraction
                                if numerator/denominator == re_num / re_den:
                                    # multiply this curious fraction into the final set
                                    final_numerator *= numerator
                                    final_denominator *= denominator

    # use the fractions module to reduce this final product of fractions to its lowest common terms
    print(Fraction(final_numerator, final_denominator))


if __name__ == '__main__':
    main()
