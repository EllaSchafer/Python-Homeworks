def ack(m, n):
    """
             { n + 1 ,                if m = 0
    A(m,n) = { A(m-1,1),              if m > 0 and n = 0
             { A(m - 1, A(m, n - 1)), if m > o and n > 0
    solves the ackerman function with two inputs using recursive functions
    :param m: variable m in the ackerman function
    :param n: variable n in the ackerman function
    :return: results of the ackerman function
    """
    if m == 0:
        return n + 1

    elif m > 0 and n == 0:
        m = m - 1
        return ack(m, 1)

    elif m > 0 and n > 0:
        m = m - 1
        n = n - 1
        return ack(m, ack(m + 1, n))


ack(3, 4)  # calls the function ack
