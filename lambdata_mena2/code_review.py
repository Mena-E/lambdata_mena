import math
import sys


def example1():
    """THIS IS A LONG COMMENT AND should be wrapped to
    fit within a 72 character limit.
    """
    some_tuple = (1, 2, 3, 'a')
    some_variable = {
        "long": 'LONG CODE LINES should be wrapped within 79 character to prevent page cutoff stuff',
        'other': [
            math.pi, 100, 200, 300, 9999292929292,
            "This IS a long string that looks gross and goes beyond what it should"
        ],
        "more": {
            "inner": "THIS whole logical line should be wrapped"
        },
        "data": [444, 5555, 222, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    }
    return some_tuple, some_variable


def example_2():
    return {"has_key() is deprecated": True}


class Example3(object):
    def __init__(self, some_string, bar=False):
        self.bar = bar
        self.some_string = some_string

    def my_bar(self):
        if self.bar:
            self.bar += 1
        else:
            self.bar *= self.bar
        return self.bar

    def my_string(self):
        self.some_string = " INDENTATION IN MULTIPLE STRINGS SHOULD NOT BE \n"
        "TOUCHED only actual code should be re-indented, THIS IS MORE CODE"
        return sys.path, self.some_string