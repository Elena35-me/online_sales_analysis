
class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product_name, product_price):
        self.products.append({'name': product_name, 'price': product_price})


    def   display_products(self):
        if not self.products:
            print("No products avaibile")
        else:
            for product in self.products:
                print(f"Product: {product['name']}, Price: {product['price']}")  

    def total_sum(self):
        total = sum(product['price'] for product in self.products)         
        print(f"Total sum of all products: {total}")   

manager = ProductManager()
manager.add_product("Laptop", 1200)
manager.add_product("Smartphone", 800)
manager.display_products()
manager.total_sum()