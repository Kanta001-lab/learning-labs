## Restaurant Management System

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         RESTAURANT MANAGER                              │
│                              (Class)                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  DATA STORAGE:                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────────────┐   │
│  │   orders     │  │  customers   │  │        daily_stats           │   │
│  │   (list)     │  │ (defaultdict)│  │        (dict)                │   │
│  ├──────────────┤  ├──────────────┤  ├──────────────────────────────┤   │
│  │ [{order1},   │  │ "Jack": [    │  │ "revenue": 0                 │   │
│  │  {order2},   │  │   {order1},  │  │ "orders_count": 0            │   │
│  │  {order3}]   │  │   {order4}]  │  │ "popular_items": Counter()   │   │
│  └──────────────┘  └──────────────┘  └──────────────────────────────┘   │
│                                                                         │
│  METHODS:                                                               │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │ add_order()        - Add new order to system                    │    │
│  │ get_customer_history() - Get all orders for a customer          │    │
│  │ get_hourly_summary()   - Group orders by hour                   │    │
│  │ print_dashboard()      - Display all statistics                 │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                         │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```