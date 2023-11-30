def is_palindrome(s):
    return s == s[::-1]  # return the boolean value of if the string == inverse of string


print(is_palindrome('stints'))
