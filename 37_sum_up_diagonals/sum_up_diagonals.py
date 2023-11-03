def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    # sum = 0
    # count = 0
    # while len(matrix) >= count:
    #     top = matrix.pop(0)
    #     bottom = matrix.pop()
    #     for each in range(0, count):
    #         top.pop(0)
    #         top.pop()
    #         bottom.pop(0)
    #         bottom.pop()
    #     sum += top.pop(0)
    #     sum += top.pop()
    #     sum += bottom.pop(0)
    #     sum += bottom.pop()
    #     count += 1
    # return sum
    
    dimension = len(matrix)
    sum = 0
    for each in range(0, dimension):
        sum += matrix[each][each] + matrix[each][dimension - 1 - each]
    return sum


    