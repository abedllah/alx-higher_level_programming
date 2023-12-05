#!/usr/bin/python3
"""check function"""


def inherits_from(obj, a_class):
    """check"""
    return isinstance(obj, a_class) and type(obj) != a_class
