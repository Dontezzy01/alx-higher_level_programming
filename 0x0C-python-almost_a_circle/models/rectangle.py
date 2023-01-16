i#!/usr/bin/python3
"""Defines a rectangle module (modules.rectangle)"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Method that init values for a rectangle object

        Args:
           width:size of the width
           height: size of the height
           x: Variable x
           y:  Variable y

        Return:
           Always nothing

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Getter and setter of width
    @property
    def width(self):
        """Getter the size of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter the size of width

        Args:
           value: Size to assign to the width

        Return:
           Always Nothing

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    # Getter and setter of height
    @property
    def height(self):
        """Getter the size of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter the size of height

        Args:
           value: Size to assign to the height

        Return:
           Always Nothing

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:

