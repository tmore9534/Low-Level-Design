# **Observer Design Pattern**

A behavioral pattern that enables a subscription mechanism to notify multiple objects automatically when the observed object changes state.

---

## **Problem Statement**

Imagine a **Customer** waiting for a new iPhone in a **Store**:

- The customer visiting daily is inefficient.
- The store emailing everyone is spammy.
- Ideal: Notify **only interested customers** when the product arrives.

---

## **Solution**

- A **Publisher (Observable/Subject)** maintains a list of **Subscribers (Observers)**.
- On an event (e.g., product restock), the publisher **notifies all subscribers**.
- **Subscribers** can **dynamically subscribe/unsubscribe**.

---

## **Real-World Analogy**

**Magazine Subscription**: You subscribe, receive new issues automatically, and can unsubscribe anytime. Non-subscribers receive nothing.

---

## **Structure**

1. **Publisher (Observable/Subject)**  
   - Maintains subscribers.  
   - Methods to **add, remove, notify** subscribers.  

2. **Subscriber (Observer)**  
   - Interface with an **`update()`** method.  
   - Implements how to respond when notified.  

3. **Concrete Publisher**  
   - Implements actual logic (e.g., an **Editor** notifying on changes).  

4. **Concrete Subscriber**  
   - Implements specific reactions (e.g., **LoggingListener**, **EmailAlertsListener**).

---

## **Pseudocode**

Enables a text editor to notify services when its state changes.  
(Refer to the class diagram on Design Gurus)  
[code](observer.py)


## Implementation Steps

1. **Identify the components**  
   - Separate **core functionality** (publisher) from **dependent functionality** (subscribers).  

2. **Define the Subscriber Interface**  
   - It should declare a method like `update()`, which the publisher will call.  

3. **Define the Publisher Interface**  
   - Add methods to **subscribe**, **unsubscribe**, and **notify subscribers**.  

4. **Implement Subscription Mechanism**  
   - Store the list of subscribers in an **abstract base class** or use **composition** if integrating into an existing hierarchy.  

5. **Create Concrete Publisher Classes**  
   - Implement the logic for **notifying all subscribers** when an event occurs.  

6. **Create Concrete Subscribers**  
   - Implement the `update()` method, where subscribers react to the notification.  

7. **Allow Runtime Configuration**  
   - Clients should be able to **dynamically add/remove subscribers** as needed. 

## **Note**

1. **Publisher**  
   - Use a common interface to manage subscriptions and notifications.  
   - Enables reuse across different publishers.  
   - Can be also integrated into existing classes or implemented separately.

2. **Subscriber**  
   - Implements a shared interface (e.g., `update()`), promoting loose coupling.  
   - Receives context or publisher reference to access required data.

- Each component can separate its business logic and use the Publisher–Subscriber mechanism via separate classes and specific methods internally.

# Benefits

- **Open/Closed Principle**: Easily add new subscribers or publishers without modifying existing code.
- **Loose Coupling**: Publishers and subscribers depend on abstractions, not each other.
- **Runtime Flexibility**: Subscribers can dynamically subscribe/unsubscribe based on need.

### Possible Problems
-  Subscribers are notified in random order.




