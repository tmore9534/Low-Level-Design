# class attiributes - declared outside the init and serves as static variables
# class methods - declared with "@classmethod" and serves as static methods. (we can call class method with object, but its of no use logically)
# static methods - u

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

# create an object
emp1 = Employee(101, "Tushar", "More", "100000")
print(Employee.no_of_employees) # 1
print(Employee.raise_amount) # 1.04

#set new raise
Employee.setRaiseAmount(2.2)
emp2 = Employee(102, "Vishal", "Roy", "100000")

print(Employee.raise_amount) # 2.2
print(emp1.raise_amount) # 2.2
print(emp2.raise_amount) # 2.2

print(Employee.no_of_employees) # 2

