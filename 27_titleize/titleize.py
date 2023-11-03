def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    lower = phrase.lower()
    phrase_list = lower.split(" ")
    capital_list = []
    for each in phrase_list:
        capital_list.append(each.replace(each[0], each[0].upper(), 1))
    return (" ").join(capital_list)
