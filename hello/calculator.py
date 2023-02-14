#!/usr/bin/env python

"""
    A set of calculator functions

    Author: <your name, <email>>
    Affl.: <your affiliation>
"""

import logging

log = logging.getLogger(__name__)


def add(i, j):
    """Add two numbers"""
    log.debug(f"Adding {i} and {j}")
    return i + j


def add_lists(i_list, j_list):
    """Add the numbers in two lists"""
    log.debug(f"Adding elements from lists {i_list} and {j_list}.")
    return [i + j for i, j in zip(i_list, j_list)]


def subtract(i, j):
    """Subtract the second number from the first"""
    log.debug(f"Subtracting {j} from {i}")
    return i - j


def multiply(i, j):
    """Multiply two numbers"""
    log.debug(f"Multiplying {i} and {j}")
    return i * j


def divide(i, j):
    """Divide the first number by the second, which must be non-zero"""
    log.debug(f"Diving {i} by {j}")
    return i / j
