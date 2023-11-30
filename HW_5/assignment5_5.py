def is_anagram(ana, gram):
    """
    determines if two srings are anagrams of eaachother
    :param ana: first string
    :param gram: second string
    :return: boolean value of whether the two are anagrams
    """
    # initializes dictionaries
    ana_hist = dict()
    gram_hist = dict()

    # histogram of the first string
    for a in ana:
        if a in ana_hist:
            ana_hist[a] += 1
        else:
            ana_hist[a] = 1

    # histogram of the second string
    for g in gram:
        if g in gram_hist:
            gram_hist[g] += 1
        else:
            gram_hist[g] = 1

    # compares the two and returns boolean true/false
    return ana_hist == gram_hist


print(is_anagram('anagram', 'gramana'))
