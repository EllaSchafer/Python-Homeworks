def is_triangle(a, b, c):
    """
    determines if the sides given form a valid triangle
    :param a: first side of the triangle
    :param b: second side of the triangle
    :param c: third side of the triangle
    :return: yes or no
    """
    if a >= b + c or b >= a + c or c >= b + a:  # if one of the sides is larger than the sum
        print("No")
    else:  # if one side isn't larger than the sum of the others do this
        print("Yes")


def isnt_triangle():
    """
    Takes user input and returns if the sides form a valid triangle
    :return: yes or no
    """

    a = input("input side 1 of triangle")
    b = input("input side 2 of triangle")
    c = input("input side 3 of triangle")

    if type(a) == 'str' or type(b) == 'str' or type(c) == 'str':
        print('invalid class, type an integer')
        isnt_triangle()
    else:
        a = int(a)
        b = int(b)
        c = int(c)
        is_triangle(a, b, c)



isnt_triangle()
