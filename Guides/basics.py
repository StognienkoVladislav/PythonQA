
import doctest
import unittest
from hypothesis import given
from hypothesis.strategies import lists, floats
# Unittest


def fun(x):
    return x+1


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)

    def test_fail(self):
        self.assertEqual(fun(3), 7)


# Doctest

def square(x):
    """Return the square of x.
    >>> square(2)
    4
    >>> square(-2)
    4
    """
    return x*x


# Hypothesis
@given(lists(floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean(xs):
    mean = sum(xs) / len(xs)
    assert min(xs) <= mean(xs) <= max(xs)


if __name__ == '__main__':
    doctest.testmod()
