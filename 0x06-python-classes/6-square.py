#!/usr/bin/python3
"""creating class square """



class Square:
    """Private instance attribute: size
    Instantiation with area method"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes attribute size and position """
        self.__size = size
        self.position = position

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

     @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Initializes attribute position"""
        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int or value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[1]) is not int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print method"""
        if (self.size == 0):
            print()
        else:
            for i in range(self.position[1]):
                print()
            for j in range(0, self.size):
                for e in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()

