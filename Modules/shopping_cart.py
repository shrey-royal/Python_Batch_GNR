# import pricing as selling_price

# net_price = selling_price.get_net_price(
#     price = 100,
#     tax_rate = 0.28,
#     discount = 0.20
# )
# print(net_price)
#########################################################

# from pricing import get_net_price as calculate_net_price, get_tax as calculate_tax

# net_price = calculate_net_price(
#     price=100,
#     tax_rate=0.01
# )
# print(net_price)
# print(calculate_tax(1000, 0.01))
#########################################################

from pricing import *
net_price = get_net_price(
    price=100,
    tax_rate=0.18,
    discount=0.05
)
print(net_price)

"""
Task:
-> A Restaurant Ordering System

A restaurant app is designed to handle orders, manage menus, and calculate bills. To make the app efficient, the developers break it into modules:

1. Menu Module
   - Responsibilities: Handle food items and categories.
   - Functions:
     - `add_item(name, price, category)`
     - `get_menu(category)`
     - `update_item(item_id, new_details)`

2. Order Module
   - Responsibilities: Manage customer orders.
   - Functions:
     - `create_order(customer_id, items)`
     - `add_item_to_order(order_id, item_id)`
     - `calculate_total(order_id)`

3. Billing Module
   - Responsibilities: Generate bills and process payments.
   - Functions:
     - `generate_bill(order_id)`
     - `process_payment(order_id, payment_method)`

-> Example
- Menu Module lists items like Pizza and Burgers.
- Order Module creates an order when a customer picks Pizza.
- Billing Module calculates the total and processes payment.

"""