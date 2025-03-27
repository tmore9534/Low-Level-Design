# Abstract class
# An abstract class is a class that cannot be instantiated and must be inherited by subclasses. 
# Simiar behviour as a java abstract class, methods are defined using @abstractMethod.
# Can have both abstract (unimplemented) and concrete (implemented) methods.
# Can have instance variables and constructors.

# Use case: when generalizing the classes,  Reuse the common method by 
# providing the abstract method to implement a specail behaviour according to subclass.
# eg. Payment class 

from abc import ABC, abstractmethod

class Payment(ABC):
    def validate(self):
        print("Common logic for having the validation")
    
    @abstractmethod
    def pay(self): #abstract method pay should be implemented according to payment methods
        pass

class UPI(Payment):
    def pay(self): 
        print("Pay using the UPI")


class Card(Payment):
    def pay(self): 
        print("Pay using the card")

# payment = Payment() # can not be intiatiated.
upi = UPI() 
card = Card()

upi.pay()
card.pay()



    


