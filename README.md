
## [Ecommerce Platform](https://github.com/iamtgiri/Ecommerce_oop)

A modular Python-based e-commerce platform that simulates an online shopping experience. This project covers essential features of an e-commerce system, including product management, order processing, customer management, and payment handling. It demonstrates modular programming concepts and can serve as a foundation for more complex applications.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Examples](#examples)
7. [Contributing](#contributing)
8. [License](#license)

## Project Overview

This project is organized as a Python package with separate modules representing different components of an e-commerce system, including:
- Products for managing inventory.
- Orders for handling customer orders.
- Customers for customer information and order placement.
- Payments for processing payments and managing transactions.

## Features

- Product Management: Create, update, and manage products with pricing and stock details.
- Order Processing: Calculate order totals, manage customer orders, and handle product stock updates.
- Customer Management: Track customer information and their orders.
- Payment Processing: Simulate payment transactions and verify payment status.

## Project Structure

The code is organized into sub-packages representing each component. Below is the folder structure:

```
Ecommerce/
│
├── customers/
│   ├── customer.py           # Customer class and methods for managing customer data
│
├── orders/
│   ├── order.py              # Order class and methods for order processing
│
├── payments/
│   ├── payment_gateway.py     # Payment processing functions
│
├── products/
│   ├── product.py            # Product class and methods for product management
│
├── __init__.py               # Main module to demonstrate the usage of the package
└── README.md                 # Project documentation
```

## Installation

To install and set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/iamtgiri/Ecommerce_oop.git
   cd ecommerce_oop
   ```

2. Install the required dependencies (if any). This project only requires Python.

3. Run the project:
   ```bash
   python -m Ecommerce
   ```

## Usage

This example demonstrates a typical usage scenario where a customer places an order and processes payment.

1. Import necessary modules:
   ```python
   from customers.customer import Customer
   from orders.order import Order
   from products.product import Product
   from payments.payment_gateway import process_payment
   ```

2. Create instances of products:
   ```python
   laptop = Product(name="Laptop", price=50000, stock_quantity=10)
   phone = Product(name="Smartphone", price=30000, stock_quantity=5)
   ```

3. Create a customer:
   ```python
   customer = Customer(customer_id=101, name="Alice", email="alice@example.com")
   ```

4. Place an order:
   ```python
   order = Order(order_id=1, customer=customer, products_order=[laptop, phone])
   total_cost = order.calculate_order_total()
   ```

5. Process payment:
   ```python
   payment_info = {'card_number': '1234-5678-9101-1121', 'expiry': '12/24'}
   payment_success = process_payment(total_cost, payment_info)
   ```

## Examples

Here’s a complete example:

```python
from customers.customer import Customer
from orders.order import Order
from products.product import Product
from payments.payment_gateway import process_payment

# Create products
laptop = Product(name="Laptop", price=50000, stock_quantity=12)
mobile = Product(name="Phone", price=17000, stock_quantity=6)

# Create a customer
customer = Customer(customer_id=1001, name="Tanmoy Giri", email="tanmoy@giri.com")

# Place an order
order = Order(order_id=5001, customer=customer, products_order=[laptop, mobile])
print(f"Total Order Amount: {order.calculate_order_total()}")

# Process payment
payment_info = {'card_number': '1234-5678-9101-1121', 'expiry': '12/24'}
if process_payment(order.calculate_order_total(), payment_info):
    for product in order.products_order:
        product.update_stock(-1)
    print("Order and payment were successful!")
else:
    print("Payment failed.")
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
