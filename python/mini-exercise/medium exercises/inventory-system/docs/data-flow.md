## Inventory System

```
 Input
    ↓
 add_order()
    ↓
 sell_item() -> Updates stocks, tracks sales, updates popular_items
                       |
                       ↓                                     
                 get_low_stock()
                       ↓                 
                 get_sales_report()        
```