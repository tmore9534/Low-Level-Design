from abc import ABC, abstractmethod
from typing import Optional


class VendingMachine:
    def __init__(self, count:int):
        if count >= 1:
            self.state = IdleState()
        else:
            self.state = OutOfStockState()
        self.count = count
    
    def insertDollar(self):
        self.state.insertDollar(self)
    
    def ejectMoney(self):
        self.state.ejectMoney(self)
    
    def despense(self):
        self.state.despense(self)
    
    def getCount(self):
        return self.count
    
    def changeState(self, state):
        self.state = state

    def doReleaseProduct(self):
        self.count -= 1
        print("Product is being released")
    
    def doEjectMoney(self):
        self.count -= 1
        print("Ejecting the money")



class State(ABC):

    @abstractmethod
    def insertDollar(self):
        pass

    @abstractmethod
    def ejectMoney(self):
        pass

    @abstractmethod
    def despense(self):
        pass



class IdleState(State):
    def insertDollar(self, vm: VendingMachine):
        print("Dollar has been accepted, processing the request")
        #move to different state
        vm.changeState(InsertedDollar())
    
    def ejectMoney(self, vm: VendingMachine):
        print("No money to eject")
    
    def despense(self):
        print("Please insert a dollar")

class InsertedDollar(State):
    def insertDollar(self, vm: VendingMachine):
        print("can not insert a dollar, canceling the request...")
        #move to different state
        vm.changeState(IdleState())
    
    def ejectMoney(self, vm: VendingMachine):
        print("Ejecting the money...")
        vm.doEjectMoney()
        vm.changeState(IdleState())
    
    def despense(self, vm: VendingMachine):
        print("despensing the product")
        if vm.getCount() > 1:
            vm.doReleaseProduct()
            vm.changeState(IdleState())
        else:
            vm.doReleaseProduct()
            vm.changeState(OutOfStockState())

class OutOfStockState(State):
    def insertDollar(self, vm: VendingMachine):
        print("Out of stock...")
        #move to different state
        vm.changeState(IdleState())
    
    def ejectMoney(self, vm: VendingMachine):
        print("No money to eject...")
    
    def despense(self, vm: VendingMachine):
        print("can not despense, system is out of stock")

    
vm = VendingMachine(2)
vm.insertDollar()
vm.despense()
vm.insertDollar()
vm.despense()
vm.insertDollar()






        