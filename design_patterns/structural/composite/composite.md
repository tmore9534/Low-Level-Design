## Composite Design Pattern 

### **Intent of the Pattern**  
- lets you compose objects into **tree structures** and work with them **as if they were individual objects**.
---

### **Problem**  
Use Composite pattern when the core model of an application can be represented as a tree.  

imagine an **ordering system** with two types of objects:  
- **Products** (simple elements)  
- **Boxes** (containers that can hold products or smaller boxes)  

An **order** might contain:  
📦 A product directly  
📦 A box containing multiple products  
📦 Nested boxes (boxes inside boxes)  

How do you calculate the **total price** of such an order efficiently?

## Naïve Solution
- You could try the direct approach: unwrap all the boxes, go over all the products, and then calculate the total.  
- It is not good, since You (client code) have to know the classes of Products and Boxes you’re going through, the nesting level of the boxes, and other details beforehand which makes the code tightly coupled.
---

### **Solution**  
The Composite pattern suggests using a **common interface** for both **Products** and **Boxes**.

- A **Product** simply returns its price.  
- A **Box** iterates over its contents, calculates the total price of each item, and returns the sum.  
- If a **Box** contains another **Box**, it **recursively** calculates the total price.  
- A **Box** can also add extra costs (e.g., packaging fees).  

✅ **Advantage**: The client doesn't need to differentiate between a **Product** or a **Box**. It **treats everything the same** through the common interface.

---

### **Implementation Steps with Example **  

![General Class Diagram](/design_patterns/resources/images/composite_pattern.png)

1. **Identify the Tree Structure**  
   - Break the system into **simple elements (leaves)** and **composite elements (containers)**.  

2. **Define a Component Interface**  
   - Ensure both leaves and containers share a **common interface** with methods like `getPrice()`.  

3. **Implement Leaf Classes**  
   - Define **simple elements** (e.g., `Product` class with `getPrice()`).  

4. **Implement Composite Class**  
   - Define **containers** (e.g., `Box` class with `getPrice()` that **aggregates prices** of its children).  

5. **Support Adding/Removing Children**  
   - Add methods to `Box` to **add or remove** items dynamically.  

6. **Ensure Recursive Behavior**  
   - When `getPrice()` is called on a **Box**, it **recursively** calculates the total.  

---

### **Structure of the Pattern**  
- **Component (Abstract Interface)**: Defines operations common to both **leaves** and **composites**.  
- **Leaf**: A basic element that does not have sub-elements.  
- **Composite**: A container that holds leaves or other composites.  
- **Client**: Works with all elements via the component interface.  

---

### Example

![Example Diagram](/design_patterns/resources/images/composite_pattern_example.png)

- [Psuedo Code](composite.py)  
 
- Client can **treat all elements uniformly** using the `Graphic` interface.

---

### **Applicability (When to Use?)**  
✅ Use when your system has a **tree-like structure**.  
✅ When you want the **client to treat individual objects & groups uniformly**.  
✅ When the **objects have recursive relationships** (e.g., UI components, file systems).  

---

### **Pros & Cons**  

✅ **Pros**  
✔ **Simplifies client code** – No need to differentiate between simple and complex objects.  
✔ **Supports recursion & polymorphism** – Handles **hierarchical** data easily.  
✔ **Open/Closed Principle** – Adding new element types **doesn’t break existing code**.  

❌ **Cons**  
✘ **Overhead** – Complex structures may add **unnecessary abstraction**.  
✘ **Difficult to restrict** – Any component can contain any other, making **validation harder**.  
