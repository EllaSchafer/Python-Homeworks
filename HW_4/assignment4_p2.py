# Exercise 6-4
def is_power(a,b):
    """
    checks if a is a power of b, in a sense, a = b ** (something)
    :param a: a possible power of b
    :param b: the number that could have a as a power
    :return: returns whether a is a power of b
    """
    if a == 1:  # zero power
        return True
    elif a == b: # if a is a 1 power
        return True
    elif a % b == 0 and (a/b) % b == 0:
        return True
    else:
        return False

print(is_power(2,2))