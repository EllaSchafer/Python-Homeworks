"""
assumptions: it is only a list of lists
"""


def nested_sum(t):
    """
    sums up nested lists
    :param t: a nested list of lists
    :return: sum of the list of lists
    """
    # initializing variables
    summy = []
    x = -1

    # de-concatenates lists
    for p1 in t:  # goes through outside list
        x += 1
        for p2 in t[x]:  # goes through internal lists one at a time
            summy.append(p2)

    summation = sum(summy)  # now can sum a non-concatenated list
    print(summation)
    return summation


nested_sum([[1, 2], [3], [4, 5, 6]])
