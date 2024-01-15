#!/usr/bin/python3
"""Class inheritan fron Base class"""
from models.base import Base


class Rectangle(Base):
    '''Represinting a rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize a new Rectangle.'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, new_value):
        if type(new_value) != int:
            raise TypeError("width must be an integer")
        if new_value <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, new_value):
        if type(new_value) != int:
            raise TypeError("height must be an integer")
        if new_value <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, new_value):
        if type(new_value) != int:
            raise TypeError("x must be integer")
        if new_value < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, new_value):
        if type(new_value) != int:
            raise TypeError("y must be in integer")
        if new_value < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_value
