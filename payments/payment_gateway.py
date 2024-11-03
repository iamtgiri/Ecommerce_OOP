import datetime

def process_payment(amount: float, payment_info: dict) -> bool:
    """
    Simulate processing a payment.

    :param amount: float - The amount to be processed
    :param payment_info: dict - Payment information (e.g., includes card number, expiry date)
    :return: bool - True if payment is successful, False otherwise
    """
    # Check if amount is valid and payment info is complete
    if amount <= 0:
        print("Payment failed: Invalid amount.")
        return False

    required_keys = ['card_number', 'expiry']
    
    # Check if all required payment info is provided
    if not all(key in payment_info for key in required_keys):
        print("Payment failed: Missing payment information.")
        return False

    # Simulate payment processing
    card_number = payment_info['card_number']
    expiry = payment_info['expiry']

    # Basic validation for demonstration purposes
    if len(card_number) != 16 or not card_number.isdigit():
        print("Payment failed: Invalid card number.")
        return False

    # Validate the expiry date
    try:
        # Assuming expiry is in MM/YY format
        expiry_month, expiry_year = map(int, expiry.split('/'))
        # Create a datetime object for the expiry date
        expiry_date = datetime.datetime(year=2000 + expiry_year, month=expiry_month, day=1)
        # Get the current date
        current_date = datetime.datetime.now()

        # Check if the card is expired
        if expiry_date < current_date:
            print("Payment failed: Card is expired.")
            return False
    except ValueError:
        print("Payment failed: Invalid expiry date format. Use MM/YY.")
        return False

    # If all checks pass, process the payment
    print(f"Processing payment of {amount} using card {card_number}.")
    print("Payment Successful!")
    return True
