"""
function named right_justify that takes a string
as a parameter and prints the string with enough leading
zeros that the last letter is in col 70
"""


def right_justify(s):
    length = len(s)  # length is a variable containing the length of the string
    space_num = 70 - length  # the amount of spaces needed to be added
    spaces = space_num * " "  # gets a string with the correct amount of spaces
    print(spaces + s)


right_justify('monty') # calls the function and the parameter is monty in this case
