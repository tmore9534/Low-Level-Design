## Facatory method Pattern
- When multiple object creations are handled in one place based on conditions, the code becomes messy and hard to maintain.
- The Factory Method Pattern provides a structured way to create objects, moving the object creation logic into a dedicated factory class or an abstract method in a superclass.
    - Factory Object: Uses a separate class (Factory) to create objects.
    - Factory Method Pattern: Defines a method in the same class (or superclass) that subclasses override to create objects. letting the subclass decide which object should be created.


## Use case 
- **Encapsulates object creation** in a dedicated place, improving maintainability and reducing redundancy.  
- **Factory Methods enable dynamic object creation** for different subclasses.  
- If creation logic is complex, a **Factory Object may be preferable** (though not a standard pattern).  
- **Supports polymorphism**, allowing client code to depend on interfaces rather than concrete implementations.  
- **Simplifies extension** by introducing new factory methods without modifying existing code.
- Client code becomes simplified.

  
## Implementation in Python with Example

General Structure:

![General Class Diagram](/design_patterns/resources/images/factory_method.png)

Example:

![Example Diagram](/design_patterns/resources/images/factory_method_example.png)


1. Define the Abstract Product (Interface or Base Class) - 
    Create a base class or interface that defines common methods for all product types.

2. Implement Concrete Product Classes - 
    Create multiple subclasses that extend the base class and provide specific implementations.

3. Create the Abstract Creator Class - 
    Define a class with an abstract factory method that must be implemented by subclasses.

4. Implement Concrete Creator Classes - 
    Implement the abstract factory method in subclasses to return specific product instances.

5. Use the Factory Method in the Client Code - 
    The client interacts only with the abstract creator, which delegates object creation to the concrete subclass
    This class also contains common operations applicable to all product objects.

Code Examples
- Factory Object : [Factory object Pattern](factory_object.py) 
- Factory Method : [Facatory method Pattern](factory_method.py) 

## **Note**  

