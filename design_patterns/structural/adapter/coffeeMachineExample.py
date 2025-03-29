# Problem statement: https://www.coursera.org/learn/design-patterns/peer/KYA1y/ungraded-assignment-adapter-pattern
from abc import ABC, abstractmethod

class CoffeeMachineInterface(ABC):
    @abstractmethod
    def chooseFirstSelection(self):
        pass

    @abstractmethod
    def chooseScondSelection(self):
        pass


class CoffeeTouchScreenAdapter(CoffeeMachineInterface):
    def __init__(self, oldVendingMachine):
        self.oldVendingMachine = oldVendingMachine
    
    @abstractmethod
    def chooseFirstSelection(self):
        self.oldVendingMachine.selectA()

    @abstractmethod
    def chooseScondSelection(self):
        self.oldVendingMachine.selectB()

class OldCoffeeMachine():
    def selectA():
        print("Pouring A")
    
    def selectB():
        print("Pouring B")

