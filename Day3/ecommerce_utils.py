# You are asked to build a simple E-commerce Billing System using Python modules.
# Create a module file named ecommerce_utils.py that contains the following functions:
# apply_discount(price, discount_percent) → applies a discount and returns the discounted price.
# add_gst(price, gst_percent=18) → adds GST (default 18%) and returns the new price.
# generate_invoice(cart, discount_percent=0, gst_percent=18) → accepts a dictionary cart (with product names as keys and prices as values) and prints a detailed invoice.
# Create a main program file named main.py that:
# Imports the ecommerce_utils module.
# Creates a shopping cart (dictionary) with at least 3 products.
# Calls the module functions to generate an invoice.
# Expected Output Example:
# ------ INVOICE ------
# Laptop          : ₹55000
# Phone           : ₹30000Headphones      : ₹2000
# ---------------------
# Subtotal: ₹87000
# After 10% discount: ₹78300.0
# After 18% GST: ₹92454.00
# ---------------------
# Thank you for shopping with u
# ecommerce_utils.py
def apply_discount(price, discount_percent):
    """Applies discount on price and returns discounted price"""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")
    return price - (price * discount_percent / 100)
def add_gst(price, gst_percent=18):
    """Adds GST on price and returns new price"""
    if gst_percent < 0:
        raise ValueError("GST percent cannot be negative")
    return price + (price * gst_percent / 100)
def generate_invoice(cart, discount_percent=0, gst_percent=18):
    """Generates and prints a detailed invoice for the shopping cart"""
    print("------ INVOICE ------")
    subtotal = 0
    for product, price in cart.items():
        print(f"{product:<15}: ₹{price}")
        subtotal += price
    print("---------------------")
    print(f"Subtotal: ₹{subtotal}")
    discounted_price = apply_discount(subtotal, discount_percent)
    if discount_percent > 0:
        print(f"After {discount_percent}% discount: ₹{discounted_price}")
    final_price = add_gst(discounted_price, gst_percent)
    print(f"After {gst_percent}% GST: ₹{final_price:.2f}")
    print("---------------------")
    print("Thank you for shopping with us!")