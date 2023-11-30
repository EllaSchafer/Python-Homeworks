"""
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

print(invert_dict(d))
"""


def invert_dict(d):
    inverse = {}
    for key in d:
        inverse.setdefault(d[key], []).append(key)
    """
    what this is saying is, inverse.set default looks for a key, if there isn't a key, make it 
    an empty list, then append the value of the key. if the value is already there it points to 
    the value, then it appends the new one
    its:
    dictionary.setdefault(key you want, what to do if the key isn't there).add the key value because you're already 
    pointing at it.
    """
    return inverse


d = {'a': 1, 'b': 2, 'c': 1, 'd': 4}
print(invert_dict(d))
