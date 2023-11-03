def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    first_letter = phrase[0]
    return phrase.replace(first_letter, first_letter.upper(), 1)