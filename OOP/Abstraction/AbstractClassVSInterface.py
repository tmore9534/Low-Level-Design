# Abstract Class vs Interface in Python

# 1. Abstract Class:
#    - Can have both abstract (unimplemented) and concrete (implemented) methods.
#    - Can have instance variables and constructors.
#    - Used when classes share common behavior (code reuse).
#    - Supports partial implementation.

# 2. Interface (Pure Abstract Class):
#    - Only has abstract methods (no concrete methods).
#    - Acts as a contract that enforces method implementation.
#    - Used when multiple unrelated classes need to follow a common structure.
#    - Supports multiple inheritance better.

# When to Use What?
# - Use Abstract Class when you want to share some common behavior among subclasses.
# - Use Interface when you want to enforce a method structure without code reuse.

# Diamond Problem in Java vs Python:
# - In Java, multiple inheritance is not allowed due to the Diamond Problem.
#   - If a class inherits from two interfaces with the same method, Java requires explicit overriding.
# - Python allows multiple inheritance but solves the Diamond Problem using Method Resolution Order (MRO).
#   - MRO follows the C3 Linearization algorithm to determine the method call order.
#   - You can check MRO using ClassName.mro() or help(ClassName).