# MVC Design Pattern

## Intent
- Separate app into **Model** (data/logic), **View** (UI), and **Controller** (input handling).
- Promotes separation of concerns and loose coupling.

## Problem
- UI and business logic are tightly coupled.
- Hard to scale, test, and maintain.

## Solution
- **Model**: Manages data and logic. Not aware of views.
- **View**: Displays data. Observes model.
- **Controller**: Handles input. Updates model and view.

## Real-World Analogy
Cashier (Controller) uses screen (View) to manage bill (Model). Screen updates when bill changes. Cashier doesn’t interact with bill directly.

## Structure
1. **Model** – State and logic.
2. **View** – UI representation.
3. **Controller** – Input handler and coordinator.

## Pseudocode Example
- `StoreOrder` → Model (extends `Observable`)
- `OrderView` → View (implements `Observer`)
- `OrderController` → Controller

## Implementation Steps
1. Create Model (observable, manages state).
2. Build View (observer, listens to model).
3. Implement Controller (handles input, updates model).

## Notes:
- Controller relies on the interface of the Model.
- View relies on the interface of the Controller (not the Model directly).
- makes the system loosely coupled and maintainable.

## Applicability

Use MVC when:

- UI and business logic should be separated.
- Multiple views share the same data.
- You need easier testing and maintenance.
- Independent development of UI and logic is needed.

## Benefits
- Separation of concerns.
- Loose coupling.
- Reusability.
- Easier testing and maintenance.
