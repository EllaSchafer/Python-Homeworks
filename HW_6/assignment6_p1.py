# assumptions: user will only put in matching upper and lowercase values
def is_anagram(str1, str2):
    """
    takes two strings and determines whether they are anagrams of each-other
    :param str1: first strings inputted
    :param str2: second string inputted
    :return: boolean value of whether the two are anagrams
    """
    # initializes dictionaries
    dict1 = {}
    dict2 = {}
    if len(str1) != len(str2):
        return False  # makes code slightly faster if they are of separate lengths
    # makes histogram of str 1
    for c in str1:
        if c in dict1:
            dict1[c] += 1
        else:
            dict1[c] = 1

    # makes histogram of str 2
    for c in str2:
        if c in dict2:
            dict2[c] += 1
        else:
            dict2[c] = 1

    return dict1 == dict2  # compares histograms


print(is_anagram('hotfoot', 'GhostDoc'))
