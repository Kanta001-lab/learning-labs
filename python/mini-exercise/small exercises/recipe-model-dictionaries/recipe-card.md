## Module: 03 Recipe Model (Dictionaries).py


#### PIZZA RECIPE CARD (Dictionary Version) 
```
┌─────────────────────────────────────────────────────┐
│ PIZZA RECIPE: make pizza                            │
├─────────────────────────────────────────────────────┤
│ INPUTS                                              │
│   pizza_type      → "pepperoni"                     │
│   pizza_topping   → "mushroom"                      │
│   pineapple       → False                           │
├─────────────────────────────────────────────────────┤
│ PROCESS                                             │
│   1. Lookup pizza type in type_map                  │
│   2. Lookup topping in topping_map                  │
│   3. Apply fallback if key not found                │
│   4. Build pizza description                        │
├─────────────────────────────────────────────────────┤
│ OUTPUT                                              │
│   🍕 Pepperoni Pizza + 🍄 Mushroom                 │
├─────────────────────────────────────────────────────┤
│ CONCEPTS                                            │
│   • Dictionary Lookup                               │
│   • .get() Fallbacks                                │
│   • Key → Value Mapping                             │
└─────────────────────────────────────────────────────┘
```
### Key Takeaway

Dictionaries act as lookup tables that transform a key
into a value in constant-time access.