
def has_duplicates(list):
    """
    determines if there is a duplicate in a list
    :param list: a list that will be checked for duplicates
    :return: true if there is a duplicate, false if not
    """
    # initializes values
    x = 1 # interating factor for strings
    y = 1 # iterating factor for int
    z = 1 # iterating factor for float
    boolean = False
    string_list = []
    int_list = []
    float_list = []
    # checks type of values
    for typ in list:
        if type(typ) == str:
            string_list.append(typ)
        elif type(typ) == int:
            int_list.append(float(typ))
        elif type(typ) == float:
            float_list.append(typ) # converts float to int
        else:
            exit('improper values')

    # sorts lists
    string_list = sorted(string_list)
    int_list = sorted(int_list)
    float_list = sorted(float_list)

    while x < len(string_list):
        if len(string_list) > 1:
            boolean = boolean or (string_list[x] == string_list[x - 1])
            x += 1
    while y < len(int_list):
        if len(int_list) > 1:
            boolean = boolean or (int_list[y] == int_list[y - 1])
            y += 1
    while y < len(int_list):
        if len(float_list) > 1:
            boolean = boolean or (int_list[y] == int_list[y - 1])
            y += 1
    return boolean


print(has_duplicates([1, 2, 3, 4, 5, 2, 4, 5, 5, 5]))
