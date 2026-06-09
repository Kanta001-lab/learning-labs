## Restaurant Management System

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         RESTAURANT MANAGER                              │
│                              (Class)                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  DATA STRUCTURES:                                                       │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │ orders (list): List of order dictionaries                       │    │
│  │ customers (defaultdict): Customer name → list of orders         │    │
│  │ hourly_orders (defaultdict): Hour → list of orders              │    │
│  │ total_revenue (float): Running total of all sales               │    │
│  │ popular_items (Counter): Item name → quantity sold              │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                         │
│  METHODS:                                                               │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │ open_restaurant()      - Opens for business                     │    │
│  │ close_restaurant()     - Closes and generates report            │    │
│  │ take_order()           - Processes a new order                  │    │
│  │ get_customer_history() - Shows customer's order history         │    │
│  │ get_hourly_summary()   - Analyzes orders by hour with bar chart │    │
│  │ get_popular_item()     - Shows top selling items                │    │
│  │ generate_daily_report()- Generates end-of-day report            │    │
│  │ simulate_busy_hour()   - Creates random orders for an hour      │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```