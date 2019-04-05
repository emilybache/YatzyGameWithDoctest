from operator import itemgetter


def small_straight(dice):
    """Score the given roll in the 'Small Straight' Yatzy category.
    """
    if sorted(dice) == [1, 2, 3, 4, 5]:
        return sum(dice)
    else:
        return 0


def large_straight(dice):
    """Score the given roll in the 'Large Straight' Yatzy category.
    """
    if sorted(dice) == [2, 3, 4, 5, 6]:
        return sum(dice)
    else:
        return 0


def chance(dice):
    """Score the given role in the 'Chance' Yatzy category"""
    return sum(dice)


def dice_counts(dice):
    """Make a dictionary of how many of each value are in the dice    """
    return {x: dice.count(x) for x in range(1, 7)}


def yatzy(dice):
    """Score the given roll in the 'Yatzy' category
    """
    counts = dice_counts(dice)
    if 5 in counts.values():
        return 50
    return 0


def full_house(dice):
    """Score the given roll in the 'Full House' category    """

    counts = dice_counts(dice)
    if 2 in counts.values() and 3 in counts.values():
        return sum(dice)
    return 0


def ones(dice):
    """Score the given roll in the 'Ones' category"""
    return dice_counts(dice)[1]


def twos(dice):
    """Score the given roll in the 'Twos' category"""
    return dice_counts(dice)[2] * 2


def threes(dice):
    """Score the given roll in the 'Threes' category"""
    return dice_counts(dice)[3] * 3


def fours(dice):
    """Score the given roll in the 'Fours' category
    """
    return dice_counts(dice)[4] * 4


def fives(dice):
    """Score the given roll in the 'Fives' category"""
    return dice_counts(dice)[5] * 5


def sixes(dice):
    """Score the given roll in the 'Sixes' category"""
    return dice_counts(dice)[6] * 6


def pair(dice):
    """Score the given roll in the 'Pair' category"""
    counts = dice_counts(dice)
    for i in [6, 5, 4, 3, 2, 1]:
        if counts[i] >= 2:
            return 2*i
    return 0


def three_of_a_kind(dice):
    """Score the given roll in the 'Three of a kind' category"""
    counts = dice_counts(dice)
    for i in [6, 5, 4, 3, 2, 1]:
        if counts[i] >= 3:
            return 3*i
    return 0


def four_of_a_kind(dice):
    """Score the given roll in the 'Four of a kind' category"""
    counts = dice_counts(dice)
    for i in [6, 5, 4, 3, 2, 1]:
        if counts[i] >= 4:
            return 4*i
    return 0


def two_pairs(dice):
    """Score the given roll in the 'Two Pairs' category"""
    counts = dice_counts(dice)
    pairs = []
    for i in [6, 5, 4, 3, 2, 1]:
        if counts[i] >= 2:
            pairs.append(i)
    if len(pairs) == 2:
        return pairs[0]*2 + pairs[1]*2
    return 0


def scores_in_categories(dice, categories=(yatzy, full_house, four_of_a_kind, three_of_a_kind, two_pairs,
                                           small_straight, large_straight,
                                           ones, twos, threes, fours, fives, sixes,
                                           chance)):
    """Score the dice in each category and return those with a non-zero score.    """
    scores = [(category(dice), category)
              for category in categories]
    return sorted(scores, reverse=True, key=itemgetter(0))


