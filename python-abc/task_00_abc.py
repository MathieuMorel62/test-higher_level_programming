from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for all animals"""

    def __init__(self):
        """Initialize the Animal object"""
        pass

    @abstractmethod
    def sound(self):
        """Method to be implemented by subclasses"""
        pass

class Dog(Animal):
    """Concrete class for dogs"""

    def sound(self):
        """Implementation of the sound method for the Dog class"""
        return "Bark"

class Cat(Animal):
    def sound(self):
        """Implementation of the sound method for the Cat class"""
        return "Meow"
