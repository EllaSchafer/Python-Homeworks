"""
do_twice - repeats a function twice
f - represents a function
v - represents a value inside of function f
print_spam - prints the word spam
print_twice - prints a sting twice
do_four - repeats a function 4 times
"""


def do_twice(f, v):  # defines do_twice with two inputs
    f(v)  # this is saying "f is a function of v"
    f(v)


def print_twice(bruce):  # bruce is a variable, it will not print bruce
    print(bruce)  # print whatever variable you are using
    print(bruce)  # repeat action above


do_twice(print_twice, "spam")  # print print_twice twice, basically double it twice


def do_four(f, v):
    do_twice(f, v)  # repeat the function twice
    do_twice(f, v)  # repeat the function twice again, totaling 4 times
