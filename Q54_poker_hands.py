from collections import Counter
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

# returns True if all cards in the hand have the same suite False otherwise
def flush(cards):
    return cards[0][1] == cards[1][1] == cards[2][1] == cards[3][1] == cards[4][1]


# returns True if the cards form a consecutive sequence
def straight(values):
    low = values[0]
    if values[1] == low + 1 and values[2] == low + 2 and values[3] == low + 3 and values[4] == low + 4:
        return True
    else:
        return False


# return True if the hand is a flush and a straight
def straight_flush(is_flush, values):
    return True if is_flush and straight(values) else False


# return True if the hand contains a flush and the value are 10 through A (10-14)
def royal_flush(is_flush, values):
    if is_flush and values[0] == 10 and values[1] == 11 and values[2] == 12 and values[3] == 13 and values[4] == 14:
        return True
    return False


# return a list of the values of the cards in the hand ordered from least to greatest
def card_vals(cards):
    return sorted([values[cards[i][0]] for i in range(5)])


# return the value of the four of a kind in the hand if exists and None otherwise
def four_of_kind(counter):
    common = counter.most_common(1)
    if common[0][1] == 4:
        return common[0][0]
    else:
        return None


# return the value of the triple in the full house if exists and None otherwise
def full_house(counter):
    common = counter.most_common(2)
    if three_of_kind(counter) and common[1][1] == 2:
        return common[0][0]
    else:
        return None


# return the value of the triple in the three of a kind if exists and None otherwise
def three_of_kind(counter):
    common = counter.most_common(1)
    if common[0][1] == 3:
        return common[0][0]
    else:
        return None


# return the values of the pairs with the larger one first and also return the 5th card if two pairs exist
def two_pair(counter):
    common = counter.most_common(3)
    if common[0][1] == 2 and common[1][1] == 2:
        return [max(common[0][0], common[1][0]), min(common[0][0], common[1][0]), common[2][0]]
    else:
        return None


# return the value of the pair and 3 non-paired cards if a pair exists and None otherwise
def one_pair(counter):
    common = counter.most_common(4)
    if common[0][1] == 2:
        return [common[0][0]] + sorted([common[1][0], common[2][0], common[3][0]], reverse=True)
    else:
        return None


def play(cards):
    p1 = cards[0:5]
    p2 = cards[5:10]
    p1_suites = flush(p1)
    p2_suites = flush(p2)
    p1_values = card_vals(p1)
    p2_values = card_vals(p2)

    # check if either hand has a royal flush, we don't check if they both do since it is known there are no ties
    if royal_flush(p1_suites, p1_values):
        return True
    if royal_flush(p2_suites, p2_values):
        return False

    # check for straight flushes
    p1_straight_flush = straight_flush(p1_suites, p1_values)
    p2_straight_flush = straight_flush(p2_suites, p2_values)
    # check if the first hand has a straight flush
    if p1_straight_flush:
        # check if the second hand also contains a straight flush
        if p2_straight_flush:
            # when both hands contain a straight flush if the first hand's is bigger return True, else return False
            return True if p1_values[4] > p2_values[4] else False
        # the first hand contains a straight flush but the second does not so the first hand wins
        else:
            return True
    # the first hand doesn't contain a straight flush, if the second does the second hand wins
    elif p2_straight_flush:
        return False

    p1_counter = Counter(p1_values)
    p2_counter = Counter(p2_values)

    # check for four of a kind
    four1 = four_of_kind(p1_counter)
    four2 = four_of_kind(p2_counter)
    # check if the first hand has four of a kind
    if four1:
        # check if the second hand has four of a kind
        if four2:
            # when both hands contain four of a kind if the first hand's is bigger return True, else return False
            return True if four1 > four2 else False
        # the first hand contains four of a kind but the second does not so the first hand wins
        else:
            return True
    # the first hand doesn't contain four of a kind, if the second does the second hand wins
    elif four2:
        return False

    # check for full house
    house1 = full_house(p1_counter)
    house2 = full_house(p2_counter)
    # check if the first hand has a full house
    if house1:
        # check if the second hand has a full house
        if house2:
            # when both hands contain full houses return True if the first hand has the larger triple else False
            return True if house1 > house2 else False
        # the first hand contains a full house but the second does not so the first hand wins
        else:
            return True
    # the first hand doesn't contain a full house, if the second does the second hand wins
    elif house2:
        return False

    # check for flushes
    # check if the first hand has a flush
    if p1_suites:
        # check if the first hand has a flush
        if p2_suites:
            # when both hands contain a flush if the first hand's is bigger return True, else return False
            return True if p1_values[4] > p2_values[4] else False
        # the first hand contains a flush and the second doesn't return True
        else:
            return True
    # the first hand doesn't contain a flush, if the second does the second hand wins
    if p2_suites:
        return False

    # check for straights
    p1_straight = straight(p1_values)
    p2_straight = straight(p2_values)
    # check if the first hand has a straight
    if p1_straight:
        # check if the first hand has a straight
        if p2_straight:
            # when both hands contain a straight if the first hand's is bigger return True, else return False
            return True if p1_values[4] > p2_values[4] else False
        # the first hand contains a straight and the second doesn't return True
        else:
            return True
    # the first hand doesn't contain a straight, if the second does the second hand wins
    if p2_straight:
        return False

    # check for three of a kind
    p1_triple = three_of_kind(p1_counter)
    p2_triple = three_of_kind(p2_counter)
    # check if the first hand has three of a kind
    if p1_triple:
        # check if the first hand has three of a kind
        if p2_triple:
            # when both hands contain three of a kind if the first hand's is bigger return True, else return False
            return True if p1_triple > p2_triple else False
        # the first hand contains three of a kind and the second doesn't return True
        else:
            return True
    # the first hand doesn't contain three of a kind, if the second does the second hand wins
    if p2_triple:
        return False

    # check for two pair
    p1_two_pair = two_pair(p1_counter)
    p2_two_pair = two_pair(p2_counter)
    # check if the first hand has two pair
    if p1_two_pair:
        # check if the first hand has two pair
        if p2_two_pair:
            # when both hands contain two pair check if the larger pair matches
            if p1_two_pair[0] == p2_two_pair[0]:
                # then check if the smaller pair matches
                if p1_two_pair[1] == p2_two_pair[1]:
                    # finally return True if the last card in the first hand is bigger else False
                    return True if p1_two_pair[2] > p2_two_pair[2] else False
                # if the smaller pair doesn't match return True if the first hand has a bigger smaller pair
                else:
                    return True if p1_two_pair[1] > p2_two_pair[1] else False
            # return True if the first hand has the larger pair and False otherwise
            else:
                return True if p1_two_pair[0] > p2_two_pair[0] else False
        # the first hand contains two pair and the second doesn't return True
        else:
            return True
    # the first hand doesn't contain two pair, if the second does the second hand wins
    if p2_two_pair:
        return False

    # check for one pair
    p1_one_pair = one_pair(p1_counter)
    p2_one_pair = one_pair(p2_counter)
    # check if the first hand has one pair
    if p1_one_pair:
        # check if the first hand has one pair
        if p2_one_pair:
            # when both hands contain one pair check if the pair matches
            if p1_one_pair[0] == p2_one_pair[0]:
                # then check if the highest non-paired card matches
                if p1_one_pair[1] == p2_one_pair[1]:
                    # then check if the next highest non-paired card matches
                    if p1_one_pair[2] == p2_one_pair[2]:
                        # return True if the last non-paired card is greater and False otherwise
                        return True if p1_one_pair[3] > p2_one_pair[3] else False
                    # middle non-paired card doesn't match return True if larger and False otherwise
                    else:
                        return True if p1_one_pair[2] > p2_one_pair[2] else False
                # largest unpaired card doesn't match return True if larger and False otherwise
                else:
                    return True if p1_one_pair[1] > p2_one_pair[1] else False
            # return True if the first player has the larger pair and False otherwise
            else:
                return True if p1_one_pair[0] > p2_one_pair[0] else False
        # the first hand contains one pair and the second doesn't return True
        else:
            return True
    # the first hand doesn't contain one pair, if the second does the second hand wins
    if p2_one_pair:
        return False

    # compare high card
    return True if p1_values[4] > p2_values[4] else False


# assumptions: games played with a single deck of cards, no replacement and no cards shared between hands, no ties
# effects of assumptions: two players cannot have three of a kind or four of a kind of the same rank (e.g. 4 kings)
# since a deck of cards with 4 kings cannot allow that
def main():
    with open('external_files/hands.txt', 'r') as f:
        player_1_wins = 0
        for hand in f:
            # strip out the newline, split on spaces, call play to play the hand, play returns True if player 1 wins
            if play(hand.replace('\n', '').split(' ')):
                player_1_wins += 1

        print(player_1_wins)


if __name__ == '__main__':
    main()
