def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

    dict = {}
    for each in nums:
        for e in nums:
            if (each + e) == goal:
                greatest = 0
                if nums.index(e) > nums.index(each):
                    greatest = nums.index(e)
                else:
                    greatest = nums.index(each)
                dict[greatest] = (e, each)
    soonest = len(nums) + 1
    for each in dict.keys():
        if each < soonest:
            soonest = each
    if soonest < len(nums):
        return dict[soonest]
    return ()
