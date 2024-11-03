# Main Module
from customers.customer import Customer
from orders.order import Order
from products.product import Product
from payments.payment_gateway import process_payment

# Create products
laptop1 = Product(name="Laptop", price=50000, stock_quantity=12)
mobile1 = Product(name="Phone", price=17000, stock_quantity=6)

# Create a customer
customer1 = Customer(customer_id=1001, name="Tanmoy Giri", email="tanmoy@giri.com")

# Create an order
order1 = Order(order_id=5001, customer=customer1, products_order=[laptop1, mobile1])

# Calculate and print the total order amount
total = order1.calculate_order_total()
print(f"\nTotal Order Amount for Order ID {order1.order_id}: {total}")

# Place the order
customer1.place_order(order1)

# Process payment
payment_info = {'card_number': '1234567812345678', 'expiry': '12/24'}
payment_success = process_payment(total, payment_info)

if payment_success:
    # Update stock if payment is successful
    for product in order1.products_order:
        product.stock_quantity -= 1  # Decrease stock by 1 for each product in the order
        print(f"Updated stock for {product.name}: {product.stock_quantity} remaining")
else:
    print("Payment failed. Please try again.")
