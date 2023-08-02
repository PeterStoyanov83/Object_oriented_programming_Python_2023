from typing import List
from a.project import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product or None:
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def remove(self, product_name: str) -> None:
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                break

    def __repr__(self) -> str:
        result = ""
        for product in self.products:
            result += f"{product}: {product.quantity}\n"
        return result
