#!/usr/bin/python3
"""creating class square """



class Square:
    """the body of the class """
    def __init__(self, size=0):
        """Initializes a new Square """
        self.__size = size

     def area(self):
        """Public instance method"""
        return (self.__size ** 2)

     @property
    def size(self):
        """Setter for square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Initializes attribute size """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
