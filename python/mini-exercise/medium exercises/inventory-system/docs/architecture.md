## Inventory System


```
┌─────────────────────────────────────────────────────────────────────────┐
│                             INVENTORY                                   │
│                              (Class)                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  DATA STORAGE:                                                          │
│  1. stock (dict): {"pizza": 50, "burger": 40, "fries":50}               │
│  2. sales (list): ["items":{"pizza", "quantity": 50, "total": 390000}]  │
│  3. popular_items (Counter): "pizza":{"items":"pizza",                  │
│                        "quantity": 50, "total": 390000}                 │
│  4. low_stock_alerts (set): adds stock name: "pizza", "burger" etc.     │
│                                                                         │
│  METHODS:                                                               │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │ add_item()        - Add's or updates item in inventory          │    │
│  │ sell_item()       - Sell's an item from the inventory           │    │
│  │ _check_restock_needed()   - Private method to check if item     │    │
│  │                                                needs restock.   │    │
│  │ get_low_stock()      - Returns items needing restock            │    │
│  │ get_sales_report()   - Generate comprehensive sales report      │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```