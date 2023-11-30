words = open("words.txt", "r")  # opens the text doc
word_list = words.read()  # gets the words from the txt file
keys = word_list.split()  # splits the words in a list


def interlock(str1, str2):
    """
    checks to see if two words are interlocking
    :param str1: first string
    :param str2: second string, must be the same length as string 1
    :return: boolean value of whether the two strings are interlock able
    """
    if len(str1) != len(str2):  # if the inputs are invalid
        print('invalid strings')
        return "invalid strings"
    # initializes interlocking strings and iteration
    strings_1 = ""
    strings_2 = ""
    x = 0
    while x < len(str1):  # interlocks the strings
        strings_1 += str1[x]
        strings_1 += str2[x]

        strings_2 += str2[x]
        strings_2 += str1[x]
        x += 1
    print(strings_1 in keys or strings_2 in keys)
    return strings_1 in keys or strings_2 in keys  # returns boolean value of if they are interlock able


interlock('a', 'a')
