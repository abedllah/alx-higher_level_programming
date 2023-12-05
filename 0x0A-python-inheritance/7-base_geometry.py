#!/usr/bin/python3
"""BaseGeometry"""

class BaseGeometry:
    """"my methodes"""

    def area(self):
        """raise exeption"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """"check value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
