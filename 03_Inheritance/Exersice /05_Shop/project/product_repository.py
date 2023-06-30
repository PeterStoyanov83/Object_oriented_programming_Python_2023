from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def remove(self, product_name: str):
        product = self.find(product_name)
        if product:
            self.products.remove(product)
        else:
            print("Product not found in the repository.")

    def __repr__(self):
        product_info = ""
        for product in self.products:
            product_info += f"{product.name}: {product.quantity}\n"
        return product_info
