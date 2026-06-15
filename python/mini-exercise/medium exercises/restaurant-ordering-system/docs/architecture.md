## Restaurant Ordering System

### System architecture: Relationships

```
┌─────────────────┐          ┌─────────────────┐
│   MenuItem      │          │     Order       │
├─────────────────┤          ├─────────────────┤
│ name            │          │ order_id        │
│ price           │          │ customer_name   │
│ category        │          │ table_number    │
│ prep_time       │          │ items: list     │
│ orders_count    │          │ order_time      │
├─────────────────┤          │ status          │
│ __str__()       │          ├─────────────────┤
└─────────────────┘          │ add_item()      │
         ▲                   │ calculate_total()│
         │                   │ estimated_prep_time()
         │ uses              │ receipt()       │
         │                   └─────────────────┘
         │                           ▲
         │                           │
┌─────────────────┐          ┌─────────────────┐
│   Restaurant    │──────────│    Kitchen      │
├─────────────────┤ contains ├─────────────────┤
│ name            │          │ name            │
│ menu: list      │          │ current_orders  │
│ orders: list    │          │ completed_orders│
│ kitchen         │          │ stations: dict  │
│ next_order_id   │          ├─────────────────┤
├─────────────────┤          │ receive_order() │
│ _setup_menu()   │          │ complete_order()│
│ show_menu()     │          └─────────────────┘
│ create_order()  │
│ submit_order()  │
│ get_order_status│
│ daily_report()  │
└─────────────────┘
```