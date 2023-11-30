def replace_with_question(message):
    """
    takes the first occurrence of a character and converts it into a question mark
    :param message: string that will be converted
    :return: message that has ?'s in place of first variable
    """
    # initializes variables
    hist = dict()
    x = 0
    message = list(message)  # turns string into a list
    mess = []

    while x < len(message):
        if (ord('a') <= ord(message[x]) <= ord('z')) or (
                ord('A') <= ord(message[x]) <= ord('Z')):  # if x is a character
            if message[x] in hist:  # if the letter has appeared before
                # hist[message[x]] += 1
                mess.append(message[x])
            else:  # adds to the histogram and appends character as '?'
                hist[message[x]] = 1
                mess.append('?')
        else:
            mess.append(message[x])  # if x is not a character
        x += 1  # keeps while loop going

    return "".join(mess)  # joins the list together as a string


print(replace_with_question('boyo!! boy man'))
