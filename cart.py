
class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product_name, product_price):
        self.cart_items.append({'name': product_name, 'price': product_price})

    def display_cart(self):
        if not self.cart_items:
            print("Cart is empty.")
        else:
            for product in self.cart_items:
                print(f"Product: {product['name']}, Price: {product['price']}")        

    def total_sum(self):
        total = sum(product['price'] for product in self.cart_items)         
        print(f"Total sum of all products: {total}")       

cart = Cart()
cart.add_to_cart("Gloves", 350)
cart.add_to_cart("Mousepad", 750)
print("\ncart products:")
cart.display_cart()
cart.total_sum    