class Product:
    def __init__(self, name: str, price: float, stock_quantity: int):
        """
        Initialize a Product instance with name, price, and stock_quantity.
        """
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
        
    def __repr__(self) -> str:
        return f"Product(name={self.name}, price={self.price}, stock_quantity={self.stock_quantity})"

    def calculate_discounted_price(self, discount_rate: float) -> float:
        """
        Calculate the discounted price of the product based on the given discount rate.
        """
        discount_amount = self.price * (discount_rate / 100)
        discounted_price = self.price - discount_amount
        return round(discounted_price, 2)
