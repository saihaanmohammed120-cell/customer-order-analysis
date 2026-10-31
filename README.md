# E-commerce Customer Order Analysis

Course project for **Python Refresher with AI** — built with **core Python only** (standard library, zero dependencies).

Analyzes 20 e-commerce orders across 6 customers, 11 products, and 3 categories — classifying products and customers, measuring category performance, and printing a formatted business insights report.

## What it does

1. **Product popularity** — ranks all 11 products by units sold
2. **Customer classification** — tiers every customer as High / Medium / Low value by total spend
3. **Category analysis** — revenue, order count, and average order value per category (Electronics, Clothing, Home Essentials)

## Python concepts demonstrated

- `dict` of `tuple`s — the product catalog (`product → (category, unit_price)`)
- `list` of `tuple`s — immutable order records (`order_id, customer, product, quantity`)
- `set` operations, `for` loops, `if` / `elif` / `else` control flow
- Clean, sectioned reporting with formatted output

## Sample output

```
1. PRODUCT POPULARITY (units sold)
 1. Wireless Earbuds       4 units
 2. Cotton T-Shirt         4 units
 ...

2. CUSTOMER CLASSIFICATION (by total spend)
Ananya Rao      Rs. 12,895   High-Value
Suresh Patel    Rs. 12,295   High-Value
 ...
```

## Run it

```bash
python analyzing_customer_orders_project.py
```

No installation needed — pure standard library. Swap the in-code sample data for a real order dataset and the processing logic works unchanged.
