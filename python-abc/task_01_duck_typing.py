from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for all shapes"""

    @abstractmethod
    def area(self):
        """Method to be implemented by subclasses"""
        pass

    @abstractmethod
    def perimeter(self):
        """Method to be implemented by subclasses"""
        pass


class Circle(Shape):
    """Concrete class for circles"""

    def __init__(self, radius):
        """Initialize the Circle object"""
        self.radius = abs(radius)

    def area(self):
        """Implementation of the area method for the Circle class"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Implementation of the perimeter method for the Circle class"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class for rectangles"""

    def __init__(self, width, height):
        """Initialize the Rectangle object"""
        self.width = width
        self.height = height

    def area(self):
        """Implementation of the area method for the Rectangle class"""
        return self.width * self.height

    def perimeter(self):
        """Implementation of the perimeter method for the Rectangle class"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Function to display information about a shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
