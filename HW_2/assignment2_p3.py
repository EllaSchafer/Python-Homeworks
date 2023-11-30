def rhombus():
    """
    prints a rhombus made of astricks
    """
    print('    *')
    print('  * * *')
    print('* * * * *')
    print('  * * *')
    print('    *')


rhombus()


def draw_rhombus(h, s):
    """
    draw_rhombus draws a rhombus with a height of h and a symbol of s,
    works for any number > 1,
    """
    num = (h - 1) // 2

    while num > 0:
        print(num * 2 * ' ' + (h - 2 * num) * (s + " "))
        num = num - 1
    if h % 2 == 0:
        print(h * (s + ' '))
        print(h * (s + ' '))
        # write an if statement for if even do this
    else:
        print(h * (s + ' '))
    if num < (h - 1):
        num = num + 1
    else:
        num = num

    while num < (h - 1):
        print(num * 2 * ' ' + (h - 2 * num) * (s + " "))
        num = num + 1


draw_rhombus(79, '&')  # draws a rhombus of & symbols that is 7 & tall


