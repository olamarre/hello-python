#!/usr/bin/env python

""" 
    A set of calculator functions

    Author: <your name, <email>>
    Affl.: <your affiliation>
"""

import logging

log = logging.getLogger(__name__)


def add(i,j):
    """Add two numbers"""
    log.info(f"Adding {i} and {j}")
    return i+j

def subtract(i,j):
    """Subtract the second number from the first"""
    log.info(f"Subtracting {j} from {i}")
    return i-j

def multiply(i,j):
    """Multiply two numbers"""
    log.info(f"Multiplying {i} and {j}")
    return i*j

def divide(i,j):
    """Divide the first number by the second, which must be non-zero"""
    log.info(f"Diving {i} by {j}")
    return i/j
