# encapsulation - bundle related attributes and behaviours for better organization and change management.
# restrict - restrict certain attribute and method for security.
# provide abstraction by hiding internal algorithms and data representation by exposing the required detail with consistent interface.

# Public - accessible anywhere i.e. inside or outside the class.
# Private - accessible only within a class.  define using Leading double underscore (__). can be made available to outside world using public methods.
# Protected - used to provide the access in subclasses and reuse them. single underscore (_) is used to define the member with protected access.
# protected is not enforced by python and used as a convention (Rule)

# Name mageling - In Python, private attributes (starting with __) are not truly private—they are only name-mangled to avoid accidental conflicts in subclasses.
# Without name mangling, a subclass could unintentionally override a private attribute from its parent class, leading to unexpected behavior.
# Python internally renames __data in Parent to _Parent__data and __data in Child to _Child__data. This prevents unintended conflicts.
# Syntax: obj._<classname>__<attribute>
# it is also used to access private memebers outside the class using obj of child. eg obj._<classname>__<attribute>. but it is not recommended
# # we can override the public and protected attributes though.

class BankAccount:
    def __init__(self, balance, interest_rate, accountHolder):
        self.accountHolder = accountHolder #Public 
        self.__balance = balance  #Private
        self.__interest_rate = 7.9

    def __setAccountBalance(self, new_amount):  #Private. internal method
        self.__balance = new_amount

    def getAccountBalance(self): #Public, method with restriction
        # verify before providing the details
        return self.__balance
    
    def _getCommonInterestRate(self): #Protected
        print("7.9")

class SavingsAccount(BankAccount):
    def __init__(self, balance, acc_type, accountHolder, interest_rate):
        super().__init__(balance, interest_rate, accountHolder)
        self.__interest_rate = interest_rate  # Public field

    def apply_interest(self):
        interest = self.getAccountBalance() * (self.__interest_rate / 100)
        print(f"Interest applied: {interest}")

# create an object
ac1 = BankAccount(20000, 7.9,  "Uday")
sac1 = SavingsAccount(10000, "savings", "Tushar", 6.7)

print(sac1.accountHolder) # Tushar - Public
sac1._getCommonInterestRate() # Protected - can be accessed through child

sac1.getAccountBalance() # 10000 - Public

#Private can not be accessed outside.
# ac1.__balance # can not be accessed here
# ac1.__setAccountBalance() #Not accessible, also not with sac1

# common private attributes gets mangled to _ClassName__attributeName to avoid the confusion
print(sac1._BankAccount__interest_rate)
print(sac1._SavingsAccount__interest_rate)




