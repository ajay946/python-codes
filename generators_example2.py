"""
Simple example to show how generators work (also a code with 10/10 rating fro pylint testing
"""


def something():
    """
    Just pass the value to show yeild can return multiple values without coming out of function
    :return:
    """
    yield 1
    yield 2
    yield 3


for val in something():
    print(val)
