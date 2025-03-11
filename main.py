from product_manager import ProductManager
from cart import Cart 


manager = ProductManager()

manager.add_product("Headphones", 400)

manager.add_product("Monitor", 1300)

manager.display_products()

manager.total_sum()

cart = Cart()
cart.add_to_cart("Headphones", 400)
cart.add_to_cart("Monitor", 1300)
print("\ncart products:")
cart.display_cart()
cart.total_sum()