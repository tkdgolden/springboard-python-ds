def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    result = (a - b)
    if (result < 0):
        return "Second is greater"
    elif (result > 0):
        return "First is greater"
    else:
        return "Numbers are equal"