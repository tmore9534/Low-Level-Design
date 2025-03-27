# Getters (@property) - are used to access the attribute values a a property
# Setters @attribute.setter - defines the behaviour when the object is trying to set some value.
# Deleters - are used to delete/unset the attributes of the objects (del )
# it provides backword compatibility - if  objects are using email attribute, if we delete the email attribute and 
# make it as custom using @property, it doesn't affect that object

# getters and setter should provide restriction based on rules.

class Employee:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name 
        self.last_name = last_name 
        # self.email  - delete it safely and add the property decorator as a getter
    
    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split()
        self.first_name = first_name
        self.last_name = last_name
    
    @fullname.deleter
    def fullname(self):
        self.first_name = None
        self.last_name = None
        print("Deleted Successfully")
        
    # def getFullName(self):
    #     return f"{self.first_name} {self.last_name}"


emp1 = Employee(101, "Tushar", "More")

print(emp1.fullname) #getter as property

emp1.fullname = "Uday More" # setter as a property

print(emp1.fullname)

del emp1.fullname
print(emp1.fullname)
