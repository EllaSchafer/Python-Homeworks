# Exercise 7-2

# a friend of mine told me that eval is very dangerous
def eval_loop():
    """
    evaluates a loop continually until the user wishes to stop
    :return: what is evaluated
    """
    inp = input('enter value')
    ev = 0
    if inp == 'done':  # special case for if done entered first
        print('nothing was entered')
        return "nothing was entered"
    while inp != 'done':  # while the user wants to continue to do this
        ev = eval(inp)  # takes user function and solves
        print(ev)
        inp = input('enter value')  # prompts to redo expression
    print(ev)  # after loop is broken, returns last values


eval_loop()
