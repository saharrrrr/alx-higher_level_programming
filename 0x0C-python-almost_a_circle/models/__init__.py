#!/usr/bin/python3
"""Moduls for base class"""


class Base:
    """will be our base class"""

    __nb_objects = 0
    
    def __init__(self, id=None):
        """Constructur"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
