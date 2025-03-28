## Facade Design Pattern
- As systems grow, their design becomes more complex, but client classes should have a simple interface for interaction. 
- The **Facade pattern** provides a **single, simplified interface (Methods)** to interact with a subsystem.  
- It is a **structural design pattern** that wraps a subsystem **without adding new functionality**.

## Use case 
- A **client class needs a simpler way** to interact with a complex system.  
- To handle instatation and redirection of the subsytem at one place.
- To **Reduce coupling** between client classes and subsystem classes by using interfaces.
- To encapsulates subsystem complexity, achieve clean and maintainable code, ensuring separation of concerns (subsytem and the client).

## Implementation in Python with Example

![Class Diagram](/design_patterns/resources/images/facadeExample.png)

**Step 1: Design the Interface** 
- `IAccount` interface defines methods for **deposits, withdrawals, and transfers**.  

**Step 2: Implement the Interface**  
- `Chequing`, `Saving`, and `Investment` classes implement `IAccount`.  
- Each class maintains an **account number and balance**.  

**Step 3: Create the Façade Class (`BankService`)**  
- Provides **simplified methods** for creating accounts and transferring money.  
- Uses a **Hashtable** to store account objects.  
- **Hides subsystem details** from the `Customer` class.  

**Step 4: Use the Façade Class in `Customer`**  
- The `Customer` class interacts **only** with `BankService`.  
- **No need to manage individual account objects manually**. 

- Code: [Facade Pattern](facade.py)

## **Note**  
- The **subsystem/interface may change** depending on the use case.  
- The **Façade class can be adapted accordingly** to accommodate such changes.  
