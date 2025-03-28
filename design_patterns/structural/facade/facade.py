# Step 1: Define the Interface
from abc import ABC, abstractmethod

class IAccount(ABC):
    """Interface for different account types"""
    
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def transfer(self, to_account, amount):
        pass


# Step 2: Implement the Interface with Different Account Types
class Chequing(IAccount):
    """Concrete implementation of a Chequing account"""
    
    def __init__(self, balance):
        self.account_number = id(self)  # Unique ID as account number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def transfer(self, to_account, amount):
        self.withdraw(amount)
        to_account.deposit(amount)


class Saving(IAccount):
    """Concrete implementation of a Savings account"""
    
    def __init__(self, balance):
        self.account_number = id(self)
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def transfer(self, to_account, amount):
        self.withdraw(amount)
        to_account.deposit(amount)


class Investment(IAccount):
    """Concrete implementation of an Investment account"""
    
    def __init__(self, balance):
        self.account_number = id(self)
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def transfer(self, to_account, amount):
        self.withdraw(amount)
        to_account.deposit(amount)


# Step 3: Create the Façade Class (BankService) 
# (candidate for implemeting the factory design pattern, separate the different object account type).
class BankService:
    """Facade class to simplify interactions with different account types"""
    
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_type, initial_balance):
        if account_type.lower() == "chequing":
            account = Chequing(initial_balance)
        elif account_type.lower() == "saving":
            account = Saving(initial_balance)
        elif account_type.lower() == "investment":
            account = Investment(initial_balance)
        else:
            print("Invalid account type!")
            return None
        
        self.accounts[account.account_number] = account
        return account.account_number

    def transfer_money(self, from_acc_num, to_acc_num, amount):
        from_account = self.accounts.get(from_acc_num)
        to_account = self.accounts.get(to_acc_num)

        if from_account and to_account:
            from_account.transfer(to_account, amount)
            print(f"Transferred {amount} successfully!")
        else:
            print("Invalid account numbers!")


# Step 4: Use the Façade Class in a Client (Customer)
if __name__ == "__main__":
    bank = BankService()

    # Creating accounts
    saving_acc = bank.create_account("saving", 1000)
    investment_acc = bank.create_account("investment", 500)

    # Transferring money
    bank.transfer_money(saving_acc, investment_acc, 200)