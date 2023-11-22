#!/usr/bin/python3
"""creating class square """



class Square:
    """Private instance attribute: size
    Instantiation with area method"""

    def __init__(self, size=0):
        """Initializes attribute size"""
        self.__size = size

    def area(self):
        """Calculate area of square"""
        return self.__size * self.__size

    @property
    def _size(self):
        """Getter for square"""
        return self.__size

    @_size.setter
    def size(self, value):
        """Setter for square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer, not {}".format(type(value).__name__))
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()
        if self.size <= 0:
            print()
