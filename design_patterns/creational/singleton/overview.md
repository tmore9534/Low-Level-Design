## Singleton
- Ensures a single instance of a class is shared globally.
- Provides controlled access to the instance.
- [read more](https://refactoring.guru/design-patterns/singleton)

### Implementation in Python

- Custom metaclass can be used to create a singleton class in python.
- The type metaclass creates a new object every time. To control this, override its \__call__() method. 
- other ways to implement includes class variables with the getInstance(), decorators etc.

[Learn more aabout the metaclasses and meta programming](https://www.geeksforgeeks.org/metaprogramming-metaclasses-python/)

[Check implementation with sample code](https://refactoring.guru/design-patterns/singleton/python/example#example-0)

### Use case
- when a class in your program should have just a single instance available to all clients.
    - eg. a single database object shared by different parts of the program.
- Stricter control over global variables. Unlike global variables, it ensures a single instance that cannot be replaced by anything except the class itself

### Example 
- Creating a database connection with a single shared instance to avoid multiple unnecessary connections.
- [Singleton Pattern](db_singleton_example.py)