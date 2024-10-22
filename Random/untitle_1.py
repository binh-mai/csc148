def only_evens(lst: list[list[int]]) -> list[list[int]]:

    """
    >>> only_evens([[1, 2, 4], [4, 0, 6], [22, 4, 3], [2]])
    [[4, 0, 6], [2]]
    """

    for sublist in lst:
        for num in sublist:
            if num % 2 != 0:
                lst.remove(sublist)

    return lst
