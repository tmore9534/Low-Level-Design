# Mediator Design Pattern

## Intent
> “Define an object that encapsulates how a set of objects interact.
- Reduces chaotic dependencies between components.
- Promotes loose coupling by centralizing communication via a mediator.

---

## Problem It Solves
Without Mediator:
- Components (like buttons, text fields, checkboxes) are tightly coupled.
- Changes in one element may break others.
- Components become non-reusable due to hidden interdependencies.

---

## Solution
- Introduce a mediator object that controls and coordinates communication.
- Components no longer interact directly; they notify the mediator, which then performs actions or delegates tasks.

> Think of it like a team where no one talks to each other directly — they go through a manager (mediator).

---

## Real World Analogy
- Air Traffic Control Tower: Pilots (components) don’t talk directly. The tower (mediator) coordinates everything.

---

## Structure

1. **Mediator Interface** – Declares a `notify(sender, event)` method.
2. **Concrete Mediator** – Implements the coordination logic between components.
3. **Components** – Know only the mediator, not each other.

### Component Lifecycle:
- Component triggers → Notifies mediator → Mediator reacts (possibly involving other components).

### Psuedocode (Example)
- helps you eliminate mutual dependencies between various UI classes: buttons, checkboxes and text labels.
  (check the diagram on Design Gurus)
[code](mediator.py)


## Steps to Implement

1. **Identify tightly coupled classes**  
   Look for classes that are constantly interacting with each other and are difficult to reuse or test independently.

2. **Create a `Mediator` interface with a generic `notify` method**  
   This will define the communication contract between components and the mediator.

3. **Implement a Concrete Mediator that stores references and coordinates logic**  
   The Concrete Mediator handles the actual interaction logic between components.

4. **Modify components to use the mediator instead of talking to each other**  
   Each component should only reference the mediator and notify it when something happens.

5. **Optionally, the mediator can also instantiate/manage component lifecycles**  
   This can further simplify your architecture and consolidate control (acting somewhat like a factory or facade).


# Notes (Imp)

- Components hold only a Mediator reference, enabling reuse with different behaviors via interchangeable mediators.

- Object creation can be handled using Facade or Factory patterns based on event type and functionality.


## Applicability

- Use Mediator when you want to decouple tightly connected classes.
- Use Mediator when you want to reuse components in different contexts.
- Use Mediator when you notice you’re creating too many subclasses just to tweak inter-component behavior.

## Benefits

- Single Responsibility - Extract out communication at one place and components become independent.
- Open/Closed Principle - introduce new mediator without changing components.
- Loose coupling  
- Improved reusability of components  

## Possible Problems

- Mediator becomes the God object if not managed. 






