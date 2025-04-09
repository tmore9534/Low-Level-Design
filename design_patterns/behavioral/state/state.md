# **State Design Pattern – Concise Notes**

## **Intent**  
- allows an object to alter its behavior when its **internal state** changes, making it appear as if the object changed its class.

---

## **Problem**  
- Related to **Finite-State Machines (FSM)**: The object transitions between a finite number of states, each with different behavior.  
- **Traditional approach**: Uses **if/switch** conditionals to check the current state and execute behavior.  
- **Issue**: As states increase, conditionals become **complex and hard to maintain**.  

---

## **Solution**  
- **Encapsulate** state-specific behaviors into **separate state classes**.  
- The **context object** stores a reference to a **state object** and delegates behavior to it.  
- State objects can **transition** the context to another state.  
- Unlike the **Strategy pattern**, states **know about** and transition between each other.

---

## **Real-World Analogy**  
A **smartphone’s buttons** behave differently depending on the state:  
1. **Unlocked** → Executes various functions.  
2. **Locked** → Pressing a button opens the unlock screen.  
3. **Low battery** → Pressing a button shows the charging screen.  

---

1. **Context**  
   - Stores a reference to a **state object**.  
   - Delegates state-dependent behavior to the state object.  
   - Has a method to **change states**.  

2. **State Interface**  
   - Declares methods that all **concrete states** must implement.  

3. **Concrete States**  
   - Implements specific behavior for a given state.  
   - Can **trigger state transitions** by updating the context’s state.  

---



## **When to Use?**  
When an **object’s behavior depends on its state**, and it needs to change dynamically.  
When a **class has too many conditional statements** controlling behavior.  
To reduce the duplicate code across all the states and put it in abstract class. 

---

## **Implementation Steps**  
1. Identify the **context class** that changes behavior based on state.  
2. Define a **state interface** with state-specific methods.  
3. Create **concrete state classes**, implementing behavior for each state.  
4. Store a **reference to a state object** in the context and **delegate behavior**.  
5. Implement **state transitions** inside state classes or the context.  

---

## **Pros & Cons**  
**SRP (Single Responsibility Principle)** – Encapsulates state logic into separate classes.  
**OCP (Open/Closed Principle)** – Add new states without modifying the context.  
**Removes complex conditionals**, making the code cleaner and maintainable.  

**Increases the number of classes** in the system.  
**Context needs awareness of all states**, leading to dependencies.  


[Refactoring guru: state pattern](https://refactoring.guru/design-patterns/state)

