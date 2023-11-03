def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    phrase_set = set(phrase)
    phrase_dict = {}
    for each in phrase_set:
        phrase_dict[each] = phrase.count(each)
    return phrase_dict