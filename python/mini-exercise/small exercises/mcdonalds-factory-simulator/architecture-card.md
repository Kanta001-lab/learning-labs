## McDonald's Factory Simulator

#### MCDONALDS FACTORY CARD

```
┌────────────────────────────────────────────────────────┐
│ MCDONALDS FACTORY                                      │
│────────────────────────────────────────────────────────│
│DATA STRUCTURES:                                        │
│    orders = [ ("1", "2"), ("3", "1") ]                 │
│    MC_MENU = {"1": ("Name", price)}                    │
│    MC_SIZE = {"1": ("Size", multiplier)}               │
│    item_counts = {}                                    │
│    size_counts = {}                                    │
│────────────────────────────────────────────────────────│
│PROCESS:                                                │
│For each order in orders                                │
│    1. Look up item details in dictionary               │
│    2. Look up size details in dictionary               │
│    3. store item count and size count                  │
│    3. Calculate total = price * multiplier             │
│    4. Add to running total                             │
│    5. Display orders                                   │
│    6. Display daily order statistics                   │
│                                                        │
└────────────────────────────────────────────────────────┘
```
