## Restaurant Ordering System

## Dependencies

- Python 3.8+
- collections (standard library - no install needed)
- datetime (standard library - no install needed)

## System Overview

1. MenuItems(what customers can order)
2. Orders(what customers can actually order)
3. Kitchen(where food is prepared)
4. Restaurant (the main system that ties everything together)

## Key OOP Concepts Learned

1. Encapsulation
- Each class keeps its own data and methods
- Example: order knows how to calculate it own total
- Example: Kitchen manages its own order list

2. Composition
- Restaurant has a Kitchen (Composition)
- Restaurant has many MenuItems objects
- Order has many objects (with quantities)

3. Abstraction
- We don't need to know how kitchen prepares food
- We just call kitchen.receive_order(order)
- The complexity is hidden inside Kitchen class

4. State Management
- Each object maintains its own state
- order.status changes over time
- MenuItem.orders_count accumulates

5. Single Responsibility Principle
- MenuItem: just menu item data
- Order: customer order logic
- Kitchen: food prepared workflow
- Restaurant: overall system coordination