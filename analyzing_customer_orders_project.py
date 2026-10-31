"""
============================================================
E-COMMERCE CUSTOMER ORDER ANALYSIS
------------------------------------------------------------
Goal: classify products & customers, analyze category
performance, and generate business insights.

Data structures used     : list, tuple, dict, set
Control structures used  : for-loops, if/elif/else

Note: no dataset file was provided with the assignment, so a
representative 20-order sample (6 customers, 12 products, 3
categories) is used below. Swap in the real dataset if the
course provided one -- the processing logic doesn't change.
============================================================
"""

# ------------------------------------------------------------------
# 1. DATA STORAGE
# ------------------------------------------------------------------

# DICT of TUPLES -- product catalog: product -> (category, unit_price)
product_catalog = {
    "Wireless Earbuds":    ("Electronics", 2499),
    "Smartwatch":          ("Electronics", 5999),
    "Bluetooth Speaker":   ("Electronics", 1999),
    "Cotton T-Shirt":      ("Clothing", 599),
    "Denim Jeans":         ("Clothing", 1499),
    "Running Shoes":       ("Clothing", 2999),
    "Formal Shirt":        ("Clothing", 899),
    "Non-Stick Pan":       ("Home Essentials", 799),
    "LED Table Lamp":      ("Home Essentials", 649),
    "Cotton Bedsheet Set": ("Home Essentials", 1199),
    "Vacuum Flask":        ("Home Essentials", 349),
}

# LIST of TUPLES -- each order is an immutable record:
# (order_id, customer_name, product_name, quantity)
orders = [
    (101, "Ananya Rao",   "Wireless Earbuds",    1),
    (102, "Ravi Kumar",   "Cotton T-Shirt",      3),
    (103, "Ananya Rao",   "Smartwatch",          1),
    (104, "Divya Sharma", "Non-Stick Pan",       2),
    (105, "Karthik Iyer", "Running Shoes",       1),
    (106, "Ravi Kumar",   "Denim Jeans",         2),
    (107, "Meera Nair",   "LED Table Lamp",      1),
    (108, "Ananya Rao",   "Bluetooth Speaker",   1),
    (109, "Divya Sharma", "Cotton Bedsheet Set", 1),
    (110, "Karthik Iyer", "Formal Shirt",        2),
    (111, "Suresh Patel", "Wireless Earbuds",    2),
    (112, "Meera Nair",   "Vacuum Flask",        3),
    (113, "Ravi Kumar",   "Running Shoes",       1),
    (114, "Suresh Patel", "Smartwatch",          1),
    (115, "Divya Sharma", "Cotton T-Shirt",      1),
    (116, "Karthik Iyer", "Wireless Earbuds",    1),
    (117, "Ananya Rao",   "Cotton Bedsheet Set", 2),
    (118, "Meera Nair",   "Denim Jeans",         1),
    (119, "Suresh Patel", "LED Table Lamp",      2),
    (120, "Ravi Kumar",   "Non-Stick Pan",       1),
]

# ------------------------------------------------------------------
# 2. PROCESS ORDERS  (loops + conditionals build up the dicts/sets)
# ------------------------------------------------------------------

customer_totals  = {}   # customer -> total amount spent
product_counts   = {}   # product  -> total units sold
category_revenue = {}   # category -> total revenue
category_orders  = {}   # category -> number of orders placed

unique_customers  = set()
unique_products   = set()
unique_categories = set()

for order_id, customer, product, qty in orders:
    category, price = product_catalog[product]
    order_value = qty * price

    if customer in customer_totals:
        customer_totals[customer] += order_value
    else:
        customer_totals[customer] = order_value

    if product in product_counts:
        product_counts[product] += qty
    else:
        product_counts[product] = qty

    if category in category_revenue:
        category_revenue[category] += order_value
        category_orders[category] += 1
    else:
        category_revenue[category] = order_value
        category_orders[category] = 1

    unique_customers.add(customer)
    unique_products.add(product)
    unique_categories.add(category)

# Pro tip for later: once dict.get() feels natural, the four
# "if x in d: d[x] += v else: d[x] = v" blocks above can each be
# written as one line: d[x] = d.get(x, 0) + v

# ------------------------------------------------------------------
# 3. CUSTOMER CLASSIFICATION
# ------------------------------------------------------------------

def classify_customer(total_spend):
    if total_spend >= 10000:
        return "High-Value"
    elif total_spend >= 4000:
        return "Medium-Value"
    else:
        return "Low-Value"

customer_segments = {}
for customer, total in customer_totals.items():
    customer_segments[customer] = classify_customer(total)

# ------------------------------------------------------------------
# 4. RANKINGS
# ------------------------------------------------------------------

top_products   = sorted(product_counts.items(),   key=lambda x: x[1], reverse=True)
top_categories = sorted(category_revenue.items(), key=lambda x: x[1], reverse=True)
top_customers  = sorted(customer_totals.items(),  key=lambda x: x[1], reverse=True)

# ------------------------------------------------------------------
# 5. REPORT
# ------------------------------------------------------------------

print("=" * 60)
print("E-COMMERCE CUSTOMER ORDER ANALYSIS REPORT".center(60))
print("=" * 60)

print(f"\nTotal orders processed : {len(orders)}")
print(f"Unique customers       : {len(unique_customers)}")
print(f"Unique products        : {len(unique_products)}")
print(f"Categories              : {', '.join(sorted(unique_categories))}")

print("\n" + "-" * 60)
print("1. PRODUCT POPULARITY (units sold)")
print("-" * 60)
for rank, (product, count) in enumerate(top_products, start=1):
    print(f"{rank:>2}. {product:<22} {count} units")

print("\n" + "-" * 60)
print("2. CUSTOMER CLASSIFICATION (by total spend)")
print("-" * 60)
for customer, total in top_customers:
    segment = customer_segments[customer]
    print(f"{customer:<15} Rs.{total:>7,}   {segment}")

print("\n" + "-" * 60)
print("3. PRODUCT CATEGORY ANALYSIS")
print("-" * 60)
for category, revenue in top_categories:
    n_orders = category_orders[category]
    avg_order = revenue / n_orders
    print(f"{category:<18} Rs.{revenue:>7,} total   {n_orders} orders   Rs.{avg_order:,.0f} avg/order")

print("\n" + "-" * 60)
print("4. KEY BUSINESS INSIGHTS")
print("-" * 60)

high_count = sum(1 for s in customer_segments.values() if s == "High-Value")
med_count  = sum(1 for s in customer_segments.values() if s == "Medium-Value")
low_count  = sum(1 for s in customer_segments.values() if s == "Low-Value")
total_customers = len(customer_segments)

print(f"- Best-selling product    : {top_products[0][0]} ({top_products[0][1]} units)")
print(f"- Most profitable category: {top_categories[0][0]} (Rs.{top_categories[0][1]:,})")
print(f"- Top customer            : {top_customers[0][0]} (Rs.{top_customers[0][1]:,})")
print(f"- Customer mix            : {high_count} High-Value, {med_count} Medium-Value, {low_count} Low-Value (of {total_customers})")

print("\n" + "-" * 60)
print("5. RECOMMENDATIONS")
print("-" * 60)
print("- Prioritize inventory & marketing budget for the top category -- it drives the most revenue per order.")
print("- Build a loyalty/rewards program for High-Value customers to protect repeat revenue.")
print("- Bundle slower-moving categories with best-sellers to lift average basket size.")
print("=" * 60)