
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product name: {self.name}")
        print(f"Product price: {self.price}")
        print(f"Product quantity: {self.quantity}")

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print(f"Quantity for {self.name} update to {self.quantity}")     

product = Product("Laptop", 6578, 10)
product.display_info()
product.update_quantity(15)
product.display_info()           