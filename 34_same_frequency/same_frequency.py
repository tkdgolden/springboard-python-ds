def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    string1 = f"{num1}"
    string2 = f"{num2}"

    set1 = set(string1)
    set2 = set(string2)

    if set1 != set2:
        return False
    for each in set1:
        if string1.count(each) != string2.count(each):
            return False
    return True