def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
        return True


# print(any_lowercase1('IiI'))
"""
goes through every single letter in the string and has a seperate true/false
because it does not stop it only returns the boolean value of whether or not the 
last value in a string is lowercase.
"""

# print(any_lowercase2('C'))
"""
this goes through the length of the string, the issue here is that
it checks whether 'c' is a string, instead of the variable it checks if the string c, which never changes
is lowercase, since c is lowercase it will always return true, so in a sense this function returns
the boolean value True
"""

# print(any_lowercase3('cC'))
"""
This function, much like the first function, assigns flag a boolean value, the issue is it iterates
through the entire string and returns only the final character's boolean value, so this function
checks if the final value in a string is lowercase if it is it returns true, if not it returns false, even
if there are lowercase values in the string
"""

# print(any_lowercase4('CCCCcC'))
"""
This is a correct function for determining if there are any lowercase values in a string.
this initializes flag as false because initially before the loop starts looking at the string there are no 
lowercase characters because there are no characters. This uses boolean algebra and the or relation. if there is 
a lowercase string, it will change the value of flag to true, thus making all further values of flag true, ending
on the final value of flag being true, but if there are no lowercase values then the value will always be 
false because it will be false or false = false
"""

# print(any_lowercase5('CCccc'))
"""
this function checks whether the first value in a string is lowercase. for c, if the value is not lowercase it 
returns false, then after with no else statement returns true.
"""











