# Inheritance - Generalization and Reusabiltiy
# eg. developer extends Employee and adds the specialization
# manager also extend Employee and adds the specialization
# manager will have has a relationship with the developer (manager - as a whole)
# super() is used to refer the parent class object, initialize a parent class __init__()
# isinstance(obj1, cl1) - used to check if the obj1 is instance of cl1
# issubclass(cl1, cls2) - used to check if the cl1 is subclass of cl2

class Employee:
    raise_amount = 1.04 #static or class variable
    no_of_employees = 0 

    def __init__(self, id, first_name, last_name, pay):
        self.id = id
        self.first_name = first_name 
        self.last_name = last_name 
        self.pay = pay
        Employee.no_of_employees += 1
    
    def getFullName(self):
        return f"{self.first_name} {self.last_name}"

    # class method
    @classmethod
    def setRaiseAmount(cls, new_raise_amount):
        cls.raise_amount = new_raise_amount

    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amount)


class Developer(Employee):
    def __init__(self, id, first_name, last_name, pay, prg_lang=None):
        super().__init__(id, first_name, last_name, pay)
        self.prg_lang = prg_lang
    
    def __repr__(self):
        return f"{self.first_name} - {self.prg_lang}"

class Manager(Employee):
    def __init__(self, id, first_name, last_name, pay, devlopers = None):
        super().__init__(id, first_name, last_name, pay)

        if devlopers:
            self.developers = devlopers
        else:
            self.developers = [] # 0 or more  - has a 
    
    def addDeveloper(self, emp):
        self.developers.append(emp)

    def removeDeveloper(self, emp):
        if emp in self.developers:
            self.developers.remove(emp)
            return True
        return False
    
    def getAllDevelopers(self):
        return self.developers
    
# create an object
mg1 = Manager(201, "Mahesh", "Patil", "5000000")
dev1 = Developer(101, "Tushar", "More", "100000", "C")
dev2 = Developer(102, "Uday", "More", "200000", "Python")

print(mg1.getAllDevelopers()) # []

print(mg1.addDeveloper(dev1))
print(mg1.addDeveloper(dev2))

print(mg1.getAllDevelopers()) # list containing dev1, dev2

print(mg1.removeDeveloper(dev2))

print(mg1.getAllDevelopers()) # list containing dev2

print(isinstance(dev1, Developer)) # True
print(issubclass(Developer, Employee)) # False
print(issubclass(Employee, Developer)) # False
