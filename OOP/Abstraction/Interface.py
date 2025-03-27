# Interface:
# Python does not have a direct interface keyword, but we can create pure abstract classes (i.e., interfaces) using abc.ABC.
# Interfaces does not contain the abstract classe
# Class-level constant (acts as an interface variable) can be defined in interfaces, to share common variables for reusability

# Use case:
# 1. Define a common contract/interface to create a child classes during decomposition
# 2. multiple interfaces can be implemented to resue the abstraction and avoid abusing the child class.
# 3. Used in multiple inheritance to avoid dimaond problem, but Python also supports multiple inheritance through classes
# and usage the Method resolution ordering to avoid the confusion cause by diamond Problem

# Demonstrate reusability and specific implementation
# eg. animal -> bird, fish, Duck
# common method is make_sound(), but specific methods are fly, swim.
# also fly and swim can be used by multiple object like Duck 

from abc import ABC, abstractmethod

# Flyable Interface
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

# Swimmable Interface
class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass


class Animal(ABC):  # Abstract Base Class for all animals
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Animal(ABC):  # Abstract Base Class for all animals
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass


# Bird class - Implements Flyable
class Bird(Animal, Flyable):
    def make_sound(self):
        return f"{self.name} chirps"

    def fly(self):
        return f"{self.name} is flying high!"

# Fish class - Implements Swimmable
class Fish(Animal, Swimmable):
    def make_sound(self):
        return f"{self.name} makes bubbles"

    def swim(self):
        return f"{self.name} is swimming in the water!"

# Duck class - Implements both Flyable and Swimmable
class Duck(Animal, Flyable, Swimmable):
    def make_sound(self):
        return f"{self.name} quacks"

    def fly(self):
        return f"{self.name} is flying!"

    def swim(self):
        return f"{self.name} is swimming!"


# Creating objects
sparrow = Bird("Sparrow")
goldfish = Fish("Goldfish")
donald = Duck("Donald")

# Calling methods
print(sparrow.make_sound())  # ✅ Sparrow chirps
print(sparrow.fly())         # ✅ Sparrow is flying high!

print(goldfish.make_sound())  # ✅ Goldfish makes bubbles
print(goldfish.swim())        # ✅ Goldfish is swimming in the water!

print(donald.make_sound())  # ✅ Donald quacks
print(donald.fly())        # ✅ Donald is flying!
print(donald.swim())       # ✅ Donald is swimming!