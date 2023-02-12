#!/usr/bin/env python

"""
    Test the hello.calculator module

    Author: <yourself, <email>>
    Affl.: <your affiliation>
"""

import pytest
from hello.calculator import add, subtract, multiply, divide


def test_add():
    assert add(1,2) == 3
    assert add(4,5.5) == 9.5

def test_subtract():
    assert subtract(5,4) == 1
    assert subtract(3,8) == -5

def test_multiply():
    assert multiply(1,0) == 0
    assert multiply(2.5,3) == 7.5

def test_divide():
    assert divide(3,2) == 1.5
    with pytest.raises(ZeroDivisionError):
        divide(4,0)