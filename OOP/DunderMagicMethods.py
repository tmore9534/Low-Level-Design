# Dunder (Magic) Methods in Python (defined in the object in python)
# ✔ Predefined methods with double underscores (__method__) at the beginning and end.
# ✔ Customize built-in operations like operator overloading, attribute access, and object representation.
# ✔ Common examples:

# __init__ → Constructor (object initialization)

# __str__, __repr__ → Object representation

# __call__ → Make an instance callable like a function

# __getitem__, __setitem__ → Enable indexing (obj[index])

# __eq__, __lt__, __add__, etc. → Operator overloading (==, <, +)

# if not overriden and called, the call will fallback to object class

class Employee:
    def __init__(self, id, first_name, last_name, pay):
        # attributes - self refers to current object
        self.id = id
        self.first_name = first_name 
        self.last_name = last_name 
        self.pay = pay
    
    def getFullName(self):
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        # used for logging purpose, represent object as how it is created. eg Employee(101, "Tushar", "More", 10000)
        return f"Employee({self.id}, '{self.first_name}', '{self.last_name}', {self.pay}"

    def __str__(self):
        # used for logging purpose, represent object as how it is created. eg Employee(101, "Tushar", "More", 10000)
        return f"Employee name {self.first_name, self.last_name}"
    
    def __add__(self, other):
        return self.pay + other.pay

# create an object
emp1 = Employee(101, "Tushar", "More", 100000)
emp2 = Employee(101, "Vishal", "Roy", 200000)
0
print(emp1.getFullName())
print(emp1) 
print(repr(emp1)) #emp1.__repr__()
print(emp1 + emp2) #emp1.__add__()