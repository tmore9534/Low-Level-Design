# Template Method Design Pattern

## Intent
- Defines the skeleton of an **algorithm** in the superclass.
- Lets subclasses override specific steps without changing its structure.

## Problem and Naive Solution
- A data mining app processes different document formats (PDF, DOC, CSV).
- Code duplication in processing logic.
- Client code has multiple conditionals to handle different document types.

## Solution
- Break down the algorithm into steps inside a **template method**.
- Subclasses implement abstract steps but cannot modify the template method.
- Common steps remain in the base class, reducing duplication.

## Key Concepts
- **Abstract Steps**: Must be implemented by subclasses.
- **Optional Steps**: Have a default implementation but can be overridden.
- **Hooks**: Empty methods placed before/after crucial steps for flexibility.

## Real-World Analogy
- Mass housing construction where the basic structure is the same, but small adjustments can be made as per client needs.

## Structure

1. **Abstract Class**
   - Defines template method and algorithm steps.
2. **Concrete Classes**
   - Implement required steps but cannot modify the template method.

## Steps to Implement
1. Analyze the algorithm and break it into steps.
2. Create an **abstract class** with a **template method**.
3. Declare steps as abstract or provide default implementations.
4. Implement concrete subclasses with specific behavior.
5. Optionally, introduce hooks for additional flexibility.

## Pseudocode
[code](template_method.py)

## Applicability
- Use when parts of an algorithm should be customizable without modifying its structure.
- Useful when multiple classes share similar behavior but with **slight** variations.

## Pros and Cons
- Reduces code duplication.
- Achieved low coupling by providing common interface and customized classes to achieve SOC.

- Can be harder to maintain with too many steps.
- May violate Liskov Substitution Principle if default steps are suppressed in subclasses.
