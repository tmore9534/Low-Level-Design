# Command Design Pattern

## Intent

- This pattern turns a request into a stand-alone object, allows requests to be passed as method arguments.
- Object can be stored and used for reversible operation.
- request can be serialized, help to queue, delaye or scheduled for execution.

## Problem

A text editor with toolbar buttons for various actions risks excessive subclasses, tight GUI-business logic coupling, and code duplication across buttons, menus, and shortcuts

## Solution

- The Command Pattern decouples GUI from business logic by encapsulating requests as object (Command). 
- Object stores: objects to be called, storing the target, method, and parameters. (Commnad class and subclass)

- Instead of executing operations directly, GUI elements trigger command objects to handle operations,  
- reducing dependencies, and reusability across UI elements.

## Real-World Analogy

Consider a restaurant where a waiter takes an order (command) and delivers it to the kitchen. The chef reads the order and prepares the meal, without interacting with the customer directly. The order contains all necessary details, allowing the chef to execute it without additional clarification. Here order serves as command which should including everything to complete a task.

## Structure

1. **Sender (Invoker)**: Stores a reference to a command object and triggers its execution.
2. **Command Interface**: Declares an execution method.
3. **Concrete Command**: Implements a specific request by delegating execution to a receiver.
4. **Receiver**: Contains the actual business logic.
5. **Client**: Creates and configures command objects, associating them with senders.

## Pseudocode Example

A text editor with undo and redo operations:
[Code](undo_redo_command.py)

## implementation Steps.
1. Define Command Interface → Declare execute() method.
2. Create Concrete Commands → Implement command interface, store receiver reference, and initialize via constructor.
3. Create Receiver → Implement actual business logic.
4. Implement Sender (Invoker) → Store a command and call execute().
5. Client Code → Instantiate receiver, commands, and senders, then execute commands

### Note - for maintaing the history
- Extend Command Interface → Add undo().
- Enhance Commands → Store state for reversal.
- Create History → Maintain a command stack.
- Modify Sender → Push executed commands.
- Implement Undo → Pop from history and call undo(). 🚀

## Benefits

- **Decouples GUI from business logic**.
- **Supports undo/redo functionality**.
- **Allows requests to be queued or scheduled**.
- **Facilitates macro commands** (batch execution).
