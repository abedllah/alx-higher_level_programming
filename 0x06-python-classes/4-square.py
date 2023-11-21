#!/usr/bin/python3
"""creating class square """



class Square:
    """the body of the class """
    def __init__(self, size):
        """Initializes a new Square """
        self.__size = size

    @property
    def size(self):
        """size gitter"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

     def area(self):
        """Public instance method"""
        return (self.__size ** 2)
