#!/usr/bin/python3
    '''Module for base class.'''

class Base:
    '''A base class to our all comming classes'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructure'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
