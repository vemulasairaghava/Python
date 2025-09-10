import ecommerce_utils as eu
def main():
    cart = {
        "Laptop": 55000,
        "Phone": 30000,
        "Headphones": 2000
    }
    eu.generate_invoice(cart, discount_percent=10, gst_percent=18)
if __name__ == "__main__":
    main()