#!/usr/bin/python3
""" module for rectangle class. """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ method for area squre """
        return self.__size ** 2

    def __str__(self):
        """return string of this squre"""
        return "[Square]" + str(self.__size) + "/" + str(self.__size)
