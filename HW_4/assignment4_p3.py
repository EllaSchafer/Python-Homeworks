# Exercise 7-1
import math # used in test_square root



def mysquare(a):
    """
    returns an array of the interated guesses of the square root of a
    :param a: number we wish to find the square of
    :return: the square root of a and all iterated guesses in an array
    """
    x = 1 # initialize x
    mysqrt = []
    while True:
        mysqrt += [x]
        y = (x + a / x) / 2
        if y == x:
            break
        x = y

    return mysqrt



def test_square_root(a, x):
    x = a
    b = 0

    mysqrt_array = mysquare(a)
    print('a   mysqrt(a)   math.sqrt(a) diff')
    print('-   ---------   ------------ ----')
    for x in mysqrt_array:
        b += 1
        # gets the mysqrt array data ready to print
        neat_msqrt = str(round(mysqrt_array[b - 1],8))
        neat_msqrt += ' '*(11 - len(neat_msqrt))

        # gets the math.sqrt data ready to print
        neat_math = str(round(math.sqrt(x),8))
        neat_math += ' '*(12 - len(neat_math))

        # gets the difference of the two ready to print
        neat_diff = str(abs(mysqrt_array[b - 1]-math.sqrt(x)))

        print(float(b), neat_msqrt, neat_math,neat_diff )


test_square_root(9,3)
