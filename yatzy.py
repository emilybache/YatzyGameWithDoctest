from operator import itemgetter


def small_straight(dice):
    """Score the given roll in the 'Small Straight' Yatzy category.

    Args:
        dice: a sorted list of 5 integers indicating the dice rolled
    Returns:
        an integer score

    >>> small_straight([1,2,3,4,5])
    15
    >>> small_straight([1,2,3,4,4])
    0

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
    """Make a dictionary of how many of each value are in the dice

    >>> sorted(dice_counts([1,2,2,3,3]).items())
    [(1, 1), (2, 2), (3, 2), (4, 0), (5, 0), (6, 0)]

    This function only accepts collections containing integers:

    >>> dice_counts("12345") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError:  Can't convert 'int' object to str implicitly
    """
    return {x: dice.count(x) for x in range(1, 7)}


def yatzy(dice):
    """Score the given roll in the 'Yatzy' category

    >>> yatzy([1,1,1,1,1])
    50
    >>> yatzy([4,4,4,4,4])
    50
    >>> yatzy([4,4,4,4,1])
    0

    """
    counts = dice_counts(dice)
    if 5 in counts.values():
        return 50
    return 0


def full_house(dice):
    """Score the given roll in the 'Full House' category

    >>> full_house([1,1,2,2,2])
    8
    >>> full_house([6,6,6,2,2])
    22

    >>> full_house([1,2,3,4,5])
    0
    >>> full_house([1,2,2,1,3])
    0
    """

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
    """Score the dice in each category and return those with a non-zero score.

    >>> scores = scores_in_categories([1,1,2,2,2])
    >>> [(score, category.__name__) for (score, category) in scores]
    [(8, 'full_house'), (8, 'chance'), (6, 'three_of_a_kind'), (6, 'two_pairs'), (6, 'twos'), (2, 'ones'), (0, 'yatzy'), (0, 'four_of_a_kind'), (0, 'small_straight'), (0, 'large_straight'), (0, 'threes'), (0, 'fours'), (0, 'fives'), (0, 'sixes')]
    """
    scores = [(category(dice), category)
              for category in categories]
    return sorted(scores, reverse=True, key=itemgetter(0))


