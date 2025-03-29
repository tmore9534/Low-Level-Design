## Adapter Design Pattern
- Adapter pattern is used to connect incompatible systems by providing a compatible interface.
- It acts as a bridge between a client and an third party external system.
- we should not change the client to support the webservice, since some other subsytem might be using it.

## Use case 
- Flexibility: Allows integration of third-party libraries by providing interface and without modifying the client 
- Encapsulation: Hides incompatible components from the client
- Reusability: Enable reuse of existing incompatible components
- loose coupling: decouples the client and adaptee.


## Implementation in Python with Example

General Structure:

![General Class Diagram](/design_patterns/resources/images/adapter_pattern.png)

Example:

![Example Diagram](/design_patterns/resources/images/adapter_pattern_example.png)


1. Design the Target Interface – Defines expected methods.

2. Implement the Adapter Class – Converts client requests to a compatible format.

3. Use the Adapter in the Client – The client interacts with the adapter instead of the adaptee.
   

- Code: [Facade Pattern](adapter.py)  
