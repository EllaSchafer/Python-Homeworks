def is_palindrome(s):
    """
    determines whether s is a palindrome
    :param s: word that might be a palindrome
    :return: whether s is a palendrome, boolean
    """
    x = 0 # initializes x
    V = True # initializes V as true to get the loop going
    while x < len(s):
        if not V:  # if V is false, breaks loop
            break
        else:
            if s[x] == s[len(s) - x - 1]: # since length is one greater than the last index, an extra -1 is added
                x += 1
                V = True
            else:
                V = False
    print(V)
    return V  # at the end of the while loop, returns the boolean V


is_palindrome('palindrome')
