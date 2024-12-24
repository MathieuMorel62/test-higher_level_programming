#! /usr/bin/env python3
"""This module defines an abstract base class for animals"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses"""
        pass


class Dog(Animal):
    def sound(self):
        """Implementation of the sound method for the Dog class"""
        return "Bark"


class Cat(Animal):
    def sound(self):
        """Implementation of the sound method for the Cat class"""
        return "Meow"
