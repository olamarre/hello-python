#!/usr/bin/env python

""" 
    Test the calculator module

    Author: <yourself, <email>>
    Affl.: <your affiliation>
"""

import numpy as np
import pytest

from hello.calculator import add, add_lists, divide


def test_add():
    assert add(3, 5) == 8
    with pytest.raises(Exception):
        add([1, 2, 3], 4)


def test_add_lists():
    assert add_lists([1, 1, 1], [2, 2, 2]) == [3, 3, 3]

    # for numpy arrays, need to use:
    np.testing.assert_allclose(add_lists([1, 1, 1], [2, 2, 2]), np.array([3, 3, 3]))

    with pytest.raises(Exception):
        add_lists([1, 2, 3], 4)


def test_divide():
    assert divide(5, 2) == 2.5

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


if __name__ == "__main__":
    # only here for quick debugging: can easily run individual tests
    test_add()
    test_add_lists()
