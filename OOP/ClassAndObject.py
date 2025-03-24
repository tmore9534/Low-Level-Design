# Employee -> id, first_name, last_name, pay
# Behaviours -> getFullname()

class Employee:
    # constructor or initializer of an Object
    def __init__(self, id, first_name, last_name, pay):
        # attributes - self refers to current object
        self.id = id
        self.first_name = first_name 
        self.last_name = last_name 
        self.pay = pay
    
    #specify the getters and setters here

    # method 
    def getFullName(self):
        return f"{self.first_name} {self.last_name}"

# create an object
emp1 = Employee(101, "Tushar", "More", "100000")
print(emp1.getFullName())

# Constructors:

# Python does not support multiple types of constructors natively, can be different methods can be used to work with them. 
# default constructor
# parameterized constructor - 
#       use default arguments - Employee(self, id, first_name, last_name, pay, bonus=None)
#       variable or keyword arguments - Employee(self, id, first_name, last_name, pay, *prevCompanies)

# copy constructor:
# 1. use __copy__(self) to create and return a deep copy of an object
# 2. use copy module
#    Shallow Copy: obj2 = copy.copy(obj1)
#    DeepCopy - obj2 = copy.copy(obj2)






    



