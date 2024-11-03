from typing import List
from customers.customer import Customer  # Import at the top, since it's not in a circular reference

class Order:
    def __init__(self, order_id: int, customer: Customer, products_order: List['Product']):
        """
        Initialize an Order instance with order ID, customer, and list of products ordered.
        """
        self.order_id = order_id
        self.customer = customer
        self.products_order = products_order
        
    def calculate_order_total(self) -> float:
        """
        Calculate the total cost of the order by summing up the prices of all products in the order.
        """
        total_cost = sum(product.price for product in self.products_order)
        return round(total_cost, 2)
    
    def __repr__(self) -> str:
        return f"Order(order_id={self.order_id}, customer={self.customer.name}, total={self.calculate_order_total()})"
