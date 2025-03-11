from product_manager import ProductManager
from cart import Cart 


manager = ProductManager()

manager.add_product("Headphones", 250)

manager.add_product("Monitor", 2500)


<<<<<<< HEAD
=======
manager.total_sum()

cart = Cart()
cart.add_to_cart("Headphones", 250)
cart.add_to_cart("Monitor", 2500)
print("\ncart products:")
cart.display_cart()
cart.total_sum()
>>>>>>> add-cart-functionality
