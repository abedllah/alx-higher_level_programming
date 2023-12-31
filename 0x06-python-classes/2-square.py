#!/usr/bin/python3
"""creating class square """



class Square:
    """the body of the class """
    def __init__(self, size=0):
        """Initializes a new Square """
        if(type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
