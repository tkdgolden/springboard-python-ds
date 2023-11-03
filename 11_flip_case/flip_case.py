def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_list = []
    for each in phrase:
        if each.lower() == to_swap.lower():
            if each.isupper():
                new_list.append(each.lower())
            elif each.islower():
                new_list.append(each.upper())
            else:
                return "error"
        else:
            new_list.append(each)
    new_string = "".join(new_list)
    return new_string
