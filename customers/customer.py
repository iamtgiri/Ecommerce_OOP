from typing import List

class Customer:
    def __init__(self, customer_id: int, name: str, email: str):
        """
        Initialize a Customer instance with customer ID, name, and email.
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.orders: List['Order'] = []  # Use string annotations for type hinting
        
    def place_order(self, order: 'Order'):
        """
        Place an order for the customer and add it to the list of orders.
        """
        self.orders.append(order)
        print(f"Order {order.order_id} is placed by {self.name}")

    def __repr__(self) -> str:
        return f"Customer(customer_id={self.customer_id}, name={self.name}, email={self.email})"
